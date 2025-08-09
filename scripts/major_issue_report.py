#!/usr/bin/env python3

import os
import re
import sys
import datetime
from typing import Dict, List, Tuple

# Optional SMTP email sending if environment variables are configured
# Required env vars for email:
#   SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASSWORD, EMAIL_FROM, EMAIL_TO

def find_repo_root() -> str:
    return os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

FileMatch = Tuple[str, int, str]

class Issue:
    def __init__(self, name: str, description: str, globs: List[str], pattern: re.Pattern):
        self.name = name
        self.description = description
        self.globs = globs
        self.pattern = pattern
        self.matches: List[FileMatch] = []

    def add_match(self, path: str, lineno: int, line: str) -> None:
        self.matches.append((path, lineno, line.rstrip("\n")))


def iter_files(root: str, patterns: List[str]) -> List[str]:
    # Simple recursive walk filtered by extensions; patterns are suffixes like .cc, .hh etc
    exts = set()
    for pat in patterns:
        if pat.startswith("*."):
            exts.add(pat[1:])
        else:
            exts.add(pat)
    result = []
    for dirpath, dirnames, filenames in os.walk(root):
        # skip .git and build directories
        base = os.path.basename(dirpath)
        if base in {'.git', '.github', 'build', 'cmake-build', '.cache', '.venv'}:
            continue
        for fn in filenames:
            for ext in exts:
                if fn.endswith(ext):
                    result.append(os.path.join(dirpath, fn))
                    break
    return result


def scan(root: str) -> List[Issue]:
    issues: List[Issue] = []

    # 1) using namespace std in headers
    issues.append(Issue(
        name="Header namespace pollution (using namespace std;)",
        description="Avoid 'using namespace std;' in public headers to prevent global namespace pollution.",
        globs=["*.hh", "*.hpp", "*.h"],
        pattern=re.compile(r"\busing\s+namespace\s+std\s*;\b")
    ))

    # 2) memcpy from address-of first element [0] (UB on empty vectors/arrays)
    issues.append(Issue(
        name="Potential UB: memcpy from &vec[0] when size may be 0",
        description="Taking address of first element of a potentially empty container is undefined.",
        globs=["*.cc", "*.cpp", "*.c", "*.hh", "*.hpp", "*.h"],
        pattern=re.compile(r"memcpy\s*\([^,]+,\s*[^,]*\[[ ]*0[ ]*]\s*,")
    ))

    # 3) Suspicious sprintf usage with %i and boolean literal 'true'
    issues.append(Issue(
        name="Suspicious printf format: %i with boolean literal",
        description="Passing 'true'/'false' to %i is error-prone; pass an int or fix message.",
        globs=["*.cc", "*.cpp", "*.c", "*.hh", "*.hpp", "*.h"],
        pattern=re.compile(r"sprintf\s*\(.*%i.*\btrue\b")
    ))

    # 4) Possible null dereference on GetEntry(0)
    issues.append(Issue(
        name="Possible null dereference: GetEntry(0) without list size check",
        description="Ensure list has entries before accessing GetEntry(0).",
        globs=["*.cc", "*.cpp", "*.hh", "*.hpp", "*.h"],
        pattern=re.compile(r"GetListBox\(\)->GetEntry\(0\)->")
    ))

    # 5) strcpy usage (buffer overflow risk)
    issues.append(Issue(
        name="Unsafe C API: strcpy",
        description="Use snprintf/strlcpy or std::string to avoid overflow.",
        globs=["*.cc", "*.cpp", "*.c", "*.hh", "*.hpp", "*.h"],
        pattern=re.compile(r"\bstrcpy\s*\(")
    ))

    # 6) Specific logic bug seen: AddFullMCTrajectory called with _emptydata.mctrajcol
    issues.append(Issue(
        name="Logic: Using _emptydata.mctrajcol instead of _data.mctrajcol",
        description="Likely prevents MC trajectories from being drawn.",
        globs=["*.cc", "*.cpp", "*.hh"],
        pattern=re.compile(r"AddFullMCTrajectory\s*\(.*_emptydata\.mctrajcol")
    ))

    # Collect files
    all_files_by_issue: Dict[int, List[str]] = {}
    for idx, issue in enumerate(issues):
        files = iter_files(root, issue.globs)
        all_files_by_issue[idx] = files

    # Scan
    for idx, issue in enumerate(issues):
        for path in all_files_by_issue[idx]:
            try:
                with open(path, 'r', errors='ignore') as f:
                    for lineno, line in enumerate(f, start=1):
                        if issue.pattern.search(line):
                            issue.add_match(os.path.relpath(path, root), lineno, line)
            except Exception:
                # ignore unreadable files
                pass

    return issues


def format_report(issues: List[Issue]) -> str:
    now = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')
    lines: List[str] = []
    lines.append(f"Major issues report — {now}")
    lines.append("")
    # Summary
    lines.append("Summary:")
    for issue in issues:
        lines.append(f"- {issue.name}: {len(issue.matches)} matches")
    lines.append("")

    # Details
    for issue in issues:
        lines.append(f"=== {issue.name} ===")
        lines.append(issue.description)
        if not issue.matches:
            lines.append("No matches found.\n")
            continue
        max_show = 100
        for i, (path, lineno, text) in enumerate(issue.matches[:max_show], start=1):
            lines.append(f"{path}:{lineno}: {text.strip()}")
        if len(issue.matches) > max_show:
            lines.append(f"... and {len(issue.matches) - max_show} more")
        lines.append("")

    return "\n".join(lines)


def maybe_send_email(body: str) -> None:
    host = os.getenv('SMTP_HOST')
    port = os.getenv('SMTP_PORT')
    user = os.getenv('SMTP_USER')
    password = os.getenv('SMTP_PASSWORD')
    email_from = os.getenv('EMAIL_FROM')
    email_to = os.getenv('EMAIL_TO')

    if not all([host, port, user, password, email_from, email_to]):
        return  # Email not configured; just print to stdout

    import smtplib
    from email.mime.text import MIMEText

    msg = MIMEText(body, _subtype='plain')
    msg['Subject'] = 'Daily major issues report'
    msg['From'] = email_from
    msg['To'] = email_to

    with smtplib.SMTP(host, int(port)) as server:
        server.starttls()
        server.login(user, password)
        server.sendmail(email_from, [email_to], msg.as_string())


def main() -> int:
    repo_root = find_repo_root()
    issues = scan(repo_root)
    report = format_report(issues)
    print(report)
    maybe_send_email(report)
    return 0

if __name__ == '__main__':
    sys.exit(main())