# TrkHitReco

**Role:** First reconstruction stage on tracker digis — produces `StrawHit`/`ComboHit` collections and flags background/low-energy hits.

## Overview
TrkHitReco converts `StrawDigi`s into calibrated `StrawHit`s, combines them across panel/station into `ComboHit`s (optionally stereo), and flags low-energy or background-like hits using MVA/ANN classifiers. It is the upstream stage of the tracking flow: [[TrkHitReco]] → [[TrkPatRec]] / [[CalPatRec]] → [[TrkReco]] → [[Mu2eKinKal]].

## Key contents
- `StrawHitReco_module.cc` — digi-to-StrawHit calibration (timing, energy)
- `CombineStrawHits_module.cc`, `MakeStereoHits_module.cc` — ComboHit/stereo construction
- `FlagBkgHits_module.cc` — MVA/ANN-based background hit flagging
- `ProtonBunchTimeFromStrawDigis_module.cc` — POT timing from digis
- `TNTClusterer`, `DBSClusterer`, `Chi2Clusterer`, `BkgClusterer` — clustering strategies
- `PeakFit*`, `StereoLine`, `StereoPoint`, `CombineStereoPoints` — waveform peak fit and stereo geometry helpers
- `data/*.dat`, `data/*.weights.xml` — trained ANN/MVA weights

## Inputs / Outputs
- **Consumes:** `StrawDigiCollection`, `StrawDigiADCWaveformCollection`, `StrawResponse`, `TrackerStatus`, `ProtonBunchTime`, tracker geometry
- **Produces:** `StrawHitCollection`, `ComboHitCollection`, `StrawHitFlagCollection`, `BkgClusterCollection`, `ProtonBunchTime`

## Example usage
```
#include "Offline/TrkHitReco/fcl/prolog.fcl"
physics.producers.makeSH  : @local::TrkHitReco.StrawHitReco
physics.producers.makePH  : @local::TrkHitReco.CombineStrawHits
physics.producers.FlagBkgHits : @local::TrkHitReco.FlagBkgHits
```

## Related
- [[TrackerMC]] — produces the StrawDigis this folder consumes
- [[TrackerConditions]] — `StrawResponse`, `TrackerStatus`
- [[TrkPatRec]], [[CosmicReco]] — direct downstream pattern-recognition consumers
