# scripts

**Role:** Build-system glue and developer helper scripts invoked by CMake and by interactive developers.

## Overview
Unlike [[bin]] (user-facing shell tools), `scripts/` hosts infrastructure that the build and CI rely on: CMake modules, small build-time shell helpers, and Valgrind suppression files for Mu2e-specific false positives. It is typically picked up automatically during configure/build rather than run by hand.

## Key contents
- `build/cmake/Mu2eSwigHelper.cmake` - CMake function used to build SWIG-wrapped Python bindings.
- `build/bin/procs.sh` - small build-time shell helper.
- `valgrind/all_including_geant_callbacks.supp` - Valgrind suppressions covering Geant4/art noise.
- `CMakeLists.txt` - wires the above into the top-level build.

## Inputs / Outputs
- **Consumes:** invoked by the top-level CMake configuration and by developers running memory checks.
- **Produces:** CMake helper functions and suppression input for tooling; no data-flow output.

## Example usage
```shell
valgrind --suppressions=Offline/scripts/valgrind/all_including_geant_callbacks.supp \
         mu2e -c myJob.fcl
```

## Related
- [[bin]]
- [[ups]]
- [[boost_fix]]
