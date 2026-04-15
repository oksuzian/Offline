# TestTools

**Role:** Tiny developer-facing helper library providing toy classes used by unit tests elsewhere in Offline.

## Overview
Not a physics package. It exposes a minimal `TestClass` with instrumented constructors, a serial counter, and printout, intended to be linked by other packages when they need a "known non-trivial" C++ object to exercise container behavior, copy semantics, or persistence machinery.

## Key contents
- `inc/TestClass.hh`, `src/TestClass.cc` — instrumented toy class with two int data members and a per-instance serial number

## Inputs / Outputs
- **Consumes:** nothing
- **Produces:** a small static library linkable by test executables

## Related
- [[HelloWorld]]
- [[GeneralUtilities]]
