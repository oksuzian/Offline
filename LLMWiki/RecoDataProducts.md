# RecoDataProducts

**Role:** ROOT-persistable reconstructed data products — the event-level output of every subsystem's reco chain.

## Overview
RecoDataProducts defines the classes produced by digitization-to-reco stages: raw digis, hits, clusters/seeds, fitted tracks, and quality flags. It is the shared language between producing packages ([[TrkHitReco]], [[TrkReco]], [[CaloReco]], [[CRVReco]], [[CalPatRec]], [[Mu2eKinKal]], [[TrkPatRec]]) and consumers ([[CommonReco]], analysis ntuplers, trigger, [[Compression]]). Classes link against [[DataProducts]] for IDs and KinKal for track trajectories.

## Key contents
- Tracker digis/hits: `StrawDigi`, `StrawDigiFlag`, `StrawHit`, `StrawHitFlag`, `StrawHitPosition`, `ComboHit`, `StereoHit`, `StrawCluster`, `BkgCluster(Hit,Flag)`, `TimeCluster`, `HelixHit` (producers: [[TrkHitReco]], [[TrkPatRec]])
- Track fits & seeds: `HelixSeed`, `RobustHelix`, `HelixVal`, `KalSeed`, `KalSegment`, `KalIntersection`, `KKLoopHelix`, `KKCentralHelix`, `KKLine`, `TrkStrawHit*`, `TrkCaloHitSeed`, `TrkCaloHitPID`, `TrkQual`, `TrkFitFlag`, `TrkFitDirection`, `AlgorithmID` (producers: [[TrkReco]], [[Mu2eKinKal]], [[CalPatRec]])
- Calorimeter reco: `CaloDigi`, `CaloRecoDigi`, `CaloHit`, `CaloProtoCluster`, `CaloCluster`, `CaloTrigSeed` (producers: [[CaloReco]], [[CaloCluster]])
- CRV reco: `CrvDigi`, `CrvRecoPulse(Flags)`, `CrvCoincidenceCluster`, `CrvStatus`, `CrvDAQerror` (producers: [[CRVReco]], [[CRVResponse]])
- Cosmic / ExtMon / STM: `CosmicTrack(Seed)`, `ExtMonFNALRaw/Reco{Hit,Cluster}`, `ExtMonFNALTrk*`, `ExtMonUCITofHit`, `STMHit`, `STMWaveformDigi`, `STMMWDDigi`, `MSDHit`
- Event-level reco bookkeeping: `ProtonBunchTime`, `RecoProtonBunchIntensity`, `IntensityInfo*`, `RecoCount`, `RecoQual`, `TriggerInfo`, `MVAResult`, `PIDProduct`, `BkgQual`, `HitT0`

## Inputs / Outputs
- **Consumes:** [[DataProducts]], KinKal::Trajectory, KinKalGeom, [[Mu2eKinKal]], TrackerConditions, artdaq-core-mu2e Overlays
- **Produces:** Value classes + ROOT dictionaries; written to art events by every subsystem reco producer

## Related
- [[DataProducts]]
- [[MCDataProducts]]
- [[TrkReco]]
- [[TrkHitReco]]
- [[TrkPatRec]]
- [[CalPatRec]]
- [[Mu2eKinKal]]
- [[CaloReco]]
- [[CaloCluster]]
- [[CRVReco]]
- [[CosmicReco]]
- [[CommonReco]]
- [[Compression]]
