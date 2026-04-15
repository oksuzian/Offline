# Mu2e

**Role:** Provides the top-level `mu2e` executable that drives the art framework for all Mu2e Offline jobs.

## Overview
This folder is the main driver binary for the Offline code base; it is not the experiment or Geant4 integration. It contains a minimal `main()` that prints a banner (versions, build info) and then delegates to art's `artapp` to run modules specified in fcl. Every simulation, digitization, reconstruction, and analysis job launched in Offline runs through this executable.

## Key contents
- `src/mu2e_main.cc` - entry point, banner printing, calls `art::artapp`
- `CMakeLists.txt` - builds the `mu2e` executable via `cet_make_exec`

## Inputs / Outputs
- **Consumes:** fcl configuration files (via `mu2e -c ...`), environment variables (`ART_VERSION`, `KINKAL_VERSION`, `ROOT_VERSION`, `MUSE_STUB`, `OFFLINE_BANNER`)
- **Produces:** the `mu2e` executable; whatever art outputs the configured modules write (ROOT files, histograms, logs)

## Example usage
```
mu2e -c Offline/Mu2eG4/fcl/g4test_03.fcl -n 10
```

## Related
- [[Mu2eG4]]
- [[EventGenerator]]
- [[EventMixing]]
- [[Mu2eReco]]
