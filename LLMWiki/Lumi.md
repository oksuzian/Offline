# Lumi

**Role:** Online/offline luminosity (protons-on-target, NPOT) estimation from reconstructed tracker and calorimeter observables.

## Overview
Mu2e cannot measure the number of protons on target (NPOT) directly per microbunch, so this package reconstructs a proxy from fast reco quantities: calorimeter hit-maker output plus tracker straw hits and time clusters. `RecoNPOTMaker` combines those inputs into a per-event NPOT estimate; `RecoNPOTFilter` applies a minimum-weight cut against a calibration template (`npot_1b.root`); `NPOTAnalysis` histograms and compares the reco NPOT to the MC truth `ProtonBunchIntensity`.

## Key contents
- `src/RecoNPOTMaker_module.cc` — producer building the reco NPOT product from calo/tracker inputs
- `src/RecoNPOTFilter_module.cc` — filter based on NPOT weight and a reference ROOT file
- `src/NPOTAnalysis_module.cc` — analyzer comparing reco NPOT to MC truth PBI
- `fcl/prolog.fcl` — standard Lumi producer / filter / analyzer templates

## Inputs / Outputs
- **Consumes:** `CaloHitMakerFast` (CaloHits), `TTmakeSH` (StrawHits), `TTTZClusterFinder` (TimeClusters), `TTflagPH` (flags), `PBISim` (MC truth `ProtonBunchIntensity`)
- **Produces:** `RecoProtonBunchIntensity`-style data product, filter decision, TFileService histograms

## Related
- [[CaloReco]]
- [[TrkHitReco]]
- [[CommonMC]]
- [[Trigger]]
