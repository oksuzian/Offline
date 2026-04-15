# boost_fix

**Role:** Local shim that patches a Boost.Accumulators header compatibility issue.

## Overview
This directory ships tiny replacement headers under `accumulators/` that override a problematic Boost header seen with certain Boost/compiler combinations in Mu2e's build environment. The shim is installed as an INTERFACE library and placed on the include path ahead of the system Boost so that downstream code compiles cleanly. It is intentionally minimal and exists only until upstream fixes propagate.

## Key contents
- `accumulators/statistics.hpp` - replacement top-level accumulators header.
- `accumulators/statistics/stats.hpp` - replacement stats header.
- `CMakeLists.txt` - declares an INTERFACE library and installs the headers under the `Offline` path.

## Inputs / Outputs
- **Consumes:** N/A (header-only shim).
- **Produces:** an INTERFACE target whose include path overrides the corresponding Boost headers.

## Related
- [[ups]]
- [[scripts]]
