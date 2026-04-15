# TrackerConfig

**Role:** fhicl-validated configuration structs (`Config`) backing the tracker Prodition makers.

## Overview
This header-only folder defines the `*Config` parameter-set structs that mirror each `*Maker` in [[TrackerConditions]]. Separating configs from makers lets fcl validation, documentation, and dictionary generation live in a small leaf library that the conditions code depends on. All consumers of tracker conditions indirectly import these Config types via fhicl prolog.

## Key contents
- `AlignedTrackerConfig.hh`, `TrackerStatusConfig.hh` — alignment and status
- `StrawElectronicsConfig.hh`, `StrawPhysicsConfig.hh`, `StrawDriftConfig.hh`, `StrawResponseConfig.hh` — response chain
- `FullReadoutStrawConfig.hh`, `TrackerPanelMapConfig.hh` — auxiliary maps
- `Mu2eMaterialConfig.hh`, `Mu2eDetectorConfig.hh` — shared material/detector config blocks

## Inputs / Outputs
- **Consumes:** nothing at build time; fhicl parameter sets at run time
- **Produces:** C++ `Config` structs included by `*Maker` classes in [[TrackerConditions]]

## Related
- [[TrackerConditions]] — corresponding maker/cache implementations
- [[TrackerGeom]]
