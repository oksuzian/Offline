# TrkFilters

**Role:** art filter modules that accept/reject events based on tracker reconstruction products (time clusters, helix seeds, KalSeeds).

## Overview
TrkFilters collects lightweight `EDFilter` modules used in the trigger path and skim jobs to keep only events with physics-interesting tracker reconstruction. Each filter inspects an existing product (TimeCluster, HelixSeed, KalSeed) and applies configurable quality cuts. They are the main tracker entry points in the online trigger menu.

## Key contents
- `TimeClusterFilter_module.cc` — requires at least one qualifying `TimeCluster`
- `HelixFilter_module.cc` — cuts on `HelixSeed` parameters (momentum, nHits, chi2)
- `MultiHelixFilter_module.cc` — multi-helix variant
- `KalSeedFilter_module.cc` — post-fit filter on `KalSeed` momentum/quality

## Inputs / Outputs
- **Consumes:** `TimeClusterCollection`, `HelixSeedCollection`, `KalSeedCollection`
- **Produces:** art filter decisions (no new data products); optional diagnostics

## Example usage
```
physics.filters.kalFilter : {
  module_type : KalSeedFilter
  kalSeedCollections : [ "KKLoopHelix" ]
  minMomentum : 80.
  maxMomentum : 110.
}
```

## Related
- [[TrkPatRec]] — produces TimeCluster and HelixSeed
- [[TrkReco]] — produces merged HelixSeed/KalSeed
- [[Mu2eKinKal]] — produces final KalSeed
