# AnalysisConfig

**Role:** Header-only fhicl configuration structs shared by analysis-level code, chiefly the MVA catalog descriptor.

## Overview
Tiny interface package holding fhicl `Config` struct definitions consumed by analysis-side Proditions entities and MVA-based modules. It is built as an `INTERFACE` CMake library and only installs headers - there is no compiled source. Keeping these structs here lets both MVA training code and reconstruction/analysis modules share the exact same schema without pulling in heavier dependencies.

## Key contents
- `inc/MVACatalogConfig.hh` - fhicl schema for `MVAEntryConfig` (per-training descriptor: name, xml file, calibrated flag) and `MVACatalogConfig` (list of trainings plus `useDb`/`verbose` flags)
- `CMakeLists.txt` - INTERFACE library installing headers under `Offline/AnalysisConfig/inc`

## Inputs / Outputs
- **Consumes:** nothing at runtime (header-only)
- **Produces:** C++ types used by MVA catalog ProditionsEntity consumers (ParticleID, track quality, track-fit selection)

## Related
- [[AnalysisUtilities]]
- [[ParticleID]]
- [[ProditionsService]]
- [[TrkHitReco]]
