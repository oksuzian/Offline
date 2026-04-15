# CalPatRec

**Role:** Calorimeter-seeded track pattern recognition and related tracker hit-cleanup algorithms.

## Overview
CalPatRec is the calorimeter-seeded counterpart to [[TrkPatRec]]: it uses a `CaloCluster` to define a time peak, then finds helical tracker hits consistent with it. The package also hosts several tracker hit-level utilities (delta-ray finder, proton finder, TZ/phi cluster finders) that are shared with the general pattern-recognition chain. Outputs `HelixSeed`/`TimeCluster` products consumed by downstream Kalman fitting ([[Mu2eKinKal]], [[KalmanTests]]).

## Key contents
- `CalTimePeakFinder_module`, `CalLineTimePeakFinder_module` — build time peaks around calorimeter clusters
- `CalHelixFinder_module` + `CalHelixFinderAlg` — calo-seeded helix finder
- `AgnosticHelixFinder_module` — seedless helix finder (no calo requirement) sharing the diag infrastructure
- `DeltaFinder_module` + `DeltaFinderAlg` (+ `DeltaFinderAlg_findProtons`) — low-momentum delta-ray / proton hit tagging
- `TZClusterFinder_module`, `PhiClusterFinder_module` — time-Z and phi hit pre-clustering
- `ComboHitFilter_module`, `TZClusterFilter_module`, `PrefetchData_module` — hit I/O helpers
- `*Diag_tool` — `art::tool` diagnostics (`CalHelixFinderDiag`, `DeltaFinderDiag`, `MergePatRecDiag`, …)
- `data/v5_7_7/*.xml`, `*.tab` — MLP weights and quality tables for track-quality MVAs
- `fcl/prolog.fcl`, `fcl/prolog_common.fcl` — producers, filters, and merging sequence

## Inputs / Outputs
- **Consumes:** `ComboHitCollection`, `StrawHitFlagCollection`, `CaloClusterCollection` (from [[CaloCluster]]), [[TrackerGeom]] + [[BFieldGeom]]
- **Produces:** `TimeClusterCollection`, `HelixSeedCollection`, flagged `StrawHitFlagCollection`, diagnostic TTrees

## Example usage
```
mu2e -c Offline/CalPatRec/test/calPatRec.fcl
mu2e -c Offline/CalPatRec/test/mergePatRec.fcl
```

## Related
- [[TrkPatRec]] — tracker-seeded counterpart (merged by `MergePatRec`)
- [[CaloCluster]] — provides the seed clusters
- [[TrkReco]], [[TrkHitReco]], [[TrkFilters]] — shared tracker reco stack
- [[Mu2eKinKal]], [[KalmanTests]] — downstream Kalman fitters
