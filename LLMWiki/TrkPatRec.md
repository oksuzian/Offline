# TrkPatRec

**Role:** Tracker-only pattern recognition — finds time clusters and robust helix seeds from ComboHits.

## Overview
TrkPatRec turns flagged `ComboHit`s into track seeds without relying on the calorimeter (calo-seeded seeding lives in `CalPatRec`). It first groups hits in time (`TimeClusterFinder`, optionally phi-aware) then runs a robust helix finder to produce `HelixSeed`s. These seeds feed the merging/selection in [[TrkReco]] and ultimately the Kalman fit in [[Mu2eKinKal]].

## Key contents
- `TimeClusterFinder_module.cc`, `TimeAndPhiClusterFinder_module.cc` — time(+phi) clustering with MVA scoring
- `RobustHelixFinder_module.cc` — robust circle+linear helix finder producing `HelixSeed`
- `RobustMultiHelixFinder_module.cc` — multi-track variant
- `*Diag_tool.cc`, `*_types.hh` — diagnostic art tools
- `fcl/AmbigResolver.fcl`, `DoubletAmbigResolver.fcl`, `PanelAmbigResolver.fcl` — ambiguity-resolver configs shared by fitters
- `data/*.weights.xml` — trained MVAs for time cluster and helix-hit classification

## Inputs / Outputs
- **Consumes:** `ComboHitCollection`, `StrawHitFlagCollection`, `CaloClusterCollection` (optional seed), tracker geometry/conditions
- **Produces:** `TimeClusterCollection`, `HelixSeedCollection`, diagnostic trees

## Example usage
```
#include "Offline/TrkPatRec/fcl/prolog.fcl"
physics.producers.TimeClusterFinder : @local::TrkPatRec.TimeClusterFinder
physics.producers.RobustHelixFinder : @local::TrkPatRec.RobustHelixFinder
```

## Related
- [[TrkHitReco]] — upstream ComboHit and background-flag producer
- [[TrkReco]] — merges/selects HelixSeeds before fitting
- [[Mu2eKinKal]] — downstream Kalman fitter
- [[CaloCluster]] — optional calo-seeded time cluster
