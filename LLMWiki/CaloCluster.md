# CaloCluster

**Role:** Group calorimeter hits into physics-level clusters used for energy, position, and timing estimates of electromagnetic showers.

## Overview
Takes reconstructed `CaloHit` objects produced by [[CaloReco]] and runs seeded flood-fill clustering plus a splitting/merging pass to form `CaloCluster` data products. These clusters feed downstream physics (track-calorimeter matching, electron ID, triggers). A faster, online-friendly variant (`CaloClusterFast`) is also provided for trigger/DAQ paths.

## Key contents
- `CaloProtoClusterMaker_module` — seeded proto-cluster finder (`EminSeed`, `ExpandCut`, `EnoiseCut`, `deltaTime`) producing main/split proto-collections
- `CaloClusterMaker_module` — merges proto-clusters into final `CaloClusterCollection` using `maxDistMain`/`maxDistSplit` geometry cuts
- `CaloClusterFast_module` — streamlined one-pass clustering for trigger-level use
- `CaloTrigger_module` — cluster-level trigger decision
- `ClusterFinder` / `ClusterAssociator` / `ClusterUtils` — shared algorithms in the `CaloCluster` library
- `fcl/prolog.fcl` — standard producers table and `Reco` sequence

## Inputs / Outputs
- **Consumes:** `CaloHitCollection` (from [[CaloReco]]), calorimeter geometry from [[CalorimeterGeom]]
- **Produces:** `CaloProtoClusterCollection` (main + split), `CaloClusterCollection`

## Example usage
```fcl
#include "Offline/CaloCluster/fcl/prolog.fcl"
physics.producers.CaloProtoClusterMaker : @local::CaloCluster.CaloProtoClusterMaker
physics.producers.CaloClusterMaker      : @local::CaloCluster.CaloClusterMaker
physics.reco : [ CaloProtoClusterMaker, CaloClusterMaker ]
```

## Related
- [[CaloReco]] — upstream hit reconstruction
- [[CalorimeterGeom]] — disk/crystal geometry used by the finder
- [[CaloMC]] — truth-matching of clusters
- [[CalPatRec]] — consumes clusters as track-finding seeds
- [[CaloFilters]] — cluster-based trigger filters
