# CaloReco

**Role:** Waveform-level reconstruction: turn calorimeter digis into calibrated, merged `CaloHit`s.

## Overview
Fits each `CaloDigi` pulse (raw threshold or template fit), applies per-SiPM calibration from [[CaloConditions]], then merges same-crystal SiPM signals into `CaloHit`s with energy and time. Feeds [[CaloCluster]]. A fast path (`CaloHitMakerFast`) skips waveform fitting for trigger use.

## Key contents
- `CaloRecoDigiMaker_module` — waveform fitting (`RawProcessor` or `TemplateProcessor` strategies), producing `CaloRecoDigiCollection`
- `CaloHitMaker_module` — merges SiPM reco-digis per crystal into `CaloHitCollection`
- `CaloHitMakerFast_module` — one-pass trigger-level hit maker
- `CaloRawWFProcessor`, `CaloTemplateWFProcessor`, `CaloTemplateWFUtil` — waveform-fitting library
- `fcl/prolog.fcl`, `fcl/common.fcl` — default `Reco` producer sequence and sampling constants

## Inputs / Outputs
- **Consumes:** `CaloDigiCollection` (from [[CaloMC]] or data), `ProtonBunchTime`, `CalCalib`/`CaloDAQMap` Proditions
- **Produces:** `CaloRecoDigiCollection`, `CaloHitCollection`

## Example usage
```fcl
#include "Offline/CaloReco/fcl/prolog.fcl"
physics.producers.CaloRecoDigiMaker : @local::CaloReco.CaloRecoDigiMaker
physics.producers.CaloHitMaker      : @local::CaloReco.CaloHitMaker
physics.reco : [ CaloRecoDigiMaker, CaloHitMaker ]
```

## Related
- [[CaloMC]] — digi producer in MC
- [[CaloCluster]] — downstream clustering
- [[CaloConditions]] — calibration Proditions
- [[DAQConditions]]
