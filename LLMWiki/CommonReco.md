# CommonReco

**Role:** Cross-subsystem reconstruction glue — currently a thin home for reco-level event selection/output shaping used across tracker, calo, and CRV.

## Overview
CommonReco collects art modules that operate on already-reconstructed products but are not owned by a single subsystem. In the current tree its sole plugin is `SelectReco`, which slims reconstructed event content (tracks, hits, etc.) for downstream persistence or analysis-ready outputs. It sits between subsystem reco ([[TrkReco]], [[CaloReco]], [[CRVReco]]) and analysis/compression stages.

## Key contents
- `SelectReco_module.cc` — filters/selects reco products (tracks, hits) for persistence
- `fcl/prolog.fcl` — prolog stub for standard reco selection configurations
- Depends on [[RecoDataProducts]], [[DataProducts]], TrackerConditions, TrackerGeom

## Inputs / Outputs
- **Consumes:** [[RecoDataProducts]] (KalSeed, ComboHit, etc.), Tracker geometry and conditions via ProditionsService
- **Produces:** filtered reco collections for downstream output streams

## Related
- [[RecoDataProducts]]
- [[TrkReco]]
- [[CaloReco]]
- [[CRVReco]]
- [[Compression]]
- [[Filters]]
