# TrkReco

**Role:** Shared tracking utilities plus merging/selection of helix and KalSeed collections.

## Overview
TrkReco is the bridge layer between pattern recognition ([[TrkPatRec]], `CalPatRec`, [[CosmicReco]]) and final Kalman fitting in [[Mu2eKinKal]]. It hosts common fit helpers (`RobustHelixFit`, `TrkTimeCalculator`, `TrkUtilities`) and the art modules that merge helices from multiple finders, select preferred `KalSeed`s per track, and match reflected / duplicated tracks.

## Key contents
- `RobustHelixFit.{hh,cc}`, `RobustHelixFinderData.{hh,cc}` — circle/line helix fit engine used by finders
- `MergeHelices_module.cc` — merges HelixSeeds across finders (TPR/CPR/cosmic)
- `MergeKalSeeds_module.cc`, `SelectSameTrack_module.cc`, `SelectReflections_module.cc` — KalSeed-level merging/selection
- `TrackMatching_module.cc` — matches tracks across passes/fit hypotheses
- `TrackResolution_module.cc` — diagnostic resolution ntuple
- `KalSeedSelector`, `SimpleKalSeedSelector_tool.cc` — pluggable KalSeed selection policies
- `TrkTimeCalculator`, `TrkUtilities`, `TrkFaceData` — shared fit/time helpers
- `fcl/Particle.fcl`, `fcl/prolog.fcl` — particle-hypothesis configs reused across the cluster

## Inputs / Outputs
- **Consumes:** `HelixSeedCollection`(s), `KalSeedCollection`(s), `ComboHitCollection`, `CaloClusterCollection`, tracker conditions
- **Produces:** merged/selected `HelixSeedCollection` and `KalSeedCollection`, diagnostic trees

## Example usage
```
#include "Offline/TrkReco/fcl/prolog.fcl"
physics.producers.MergeHelices   : @local::TrkReco.MergeHelices
physics.producers.MergeKalSeeds  : @local::TrkReco.MergeKalSeeds
```

## Related
- [[TrkHitReco]] → [[TrkPatRec]] / [[CalPatRec]] → [[TrkReco]] → [[Mu2eKinKal]]
- [[CosmicReco]] — cosmic seeds also flow through merging
- [[TrkFilters]] — filters applied after selection
