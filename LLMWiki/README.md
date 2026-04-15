# LLMWiki

A folder-level wiki for `Mu2e/Offline`. One markdown file per top-level directory, plus an [index](index.md) grouped by subsystem and a chronological [log](log.md).

Inspired by Karpathy's [LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) pattern: the wiki is maintained incrementally so knowledge compounds rather than being re-derived per query.

## Scope

- **Folder-level only.** Each page describes the *purpose* of a top-level folder, its main entry points, and how it fits in the data flow. Not class-by-class.
- **Examples where natural.** A short fcl snippet or `mu2e -c ...` invocation is welcome when one is obvious from `fcl/` or `test/`; skip if forced.
- **Cross-reference** sibling folders with `[[FolderName]]` wiki-style links.

## Page schema

Every folder page lives at `LLMWiki/<FolderName>.md` and follows:

```markdown
# <FolderName>

**Role:** one-sentence purpose.

## Overview
2-4 sentences: problem solved, place in the data flow.

## Key contents
- `subdir/` or `ClassName` — what it does
- 3-6 bullets max, highest-signal entry points only

## Inputs / Outputs
- **Consumes:** data products, conditions, fcl, geometry
- **Produces:** data products, histograms, services

## Example usage
fcl snippet or `mu2e -c ...` command; skip if no natural example.

## Related
- [[SiblingFolder]] cross-refs
```

## Updating

When a folder changes meaningfully, update its page and append a dated entry to [log.md](log.md). When adding a new top-level folder, add a page and register it under the appropriate cluster in [index.md](index.md).
