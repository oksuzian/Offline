# MCDataProducts

**Role:** ROOT-persistable Monte-Carlo truth classes produced by generation, [[Mu2eG4]], digitization, and truth-matching stages.

## Overview
This package defines every MC-truth data product written to art events: particle histories, detector step aggregates, digi-level truth, and reco-to-truth association maps. It is the contract between simulation and downstream consumers (digitization, reco truth matching, [[Compression]], analysis ntuples). Classes here carry `art::Ptr`s among themselves, which is why coherent compression is nontrivial.

## Key contents
- Generation & particle history: `GenParticle`, `GenId`, `SimParticle`, `StageParticle`, `PrimaryParticle`, `ProcessCode`, `MCTrajectory`, `PhysicalVolumeInfo*`, `SimParticleRemapping`
- Beam / event-level truth: `ProtonBunchIntensity`, `ProtonBunchTimeMC`, `EventWeight`, `SumOfWeights`, `GenEventCount`, `CosmicLivetime`, `StatusG4`, `SimTimeOffset`
- Tracker truth: `StrawGasStep`, `StrawDigiMC`, `StepPointMC`, `PtrStepPointMCVector` (producers: [[Mu2eG4]], [[TrackerMC]])
- Calorimeter truth: `CaloShowerStep`, `CaloShowerSim`, `CaloShowerRO`, `CaloHitMC`, `CaloClusterMC`, `CaloEDepMC`, `CaloMCTruthAssns` (producers: [[CaloMC]])
- CRV truth: `CrvStep`, `CrvPhotons`, `CrvSiPMCharges`, `CrvDigiMC`, `CrvCoincidenceClusterMC(Assns)` (producers: [[CRVResponse]])
- Reco-to-truth links & auxiliary: `KalSeedMC`, `GenSimParticleLink`, `SurfaceStep`, `ExtMonFNALSimHit`, `ExtMonFNAL*TruthAssns`, `ScorerSummary`, `MARSInfo`

## Inputs / Outputs
- **Consumes:** [[DataProducts]] (IDs, enums), [[RecoDataProducts]] (for truth-match Ptrs)
- **Produces:** Value classes + ROOT dictionaries + optional Python (SWIG) bindings; consumed by essentially every MC and analysis module

## Related
- [[DataProducts]]
- [[RecoDataProducts]]
- [[Mu2eG4]]
- [[CommonMC]]
- [[CaloMC]]
- [[CRVResponse]]
- [[TrackerMC]]
- [[Compression]]
- [[Filters]]
