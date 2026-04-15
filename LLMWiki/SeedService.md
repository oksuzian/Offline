# SeedService

**Role:** art service that hands out guaranteed-unique random engine seeds to every module in a job.

## Overview
Centralizes random seed management so that each `(moduleLabel, instanceName)` pair gets a reproducible, unique seed derived from a configured policy. Supports `autoIncrement`, `linearMapping`, `preDefinedOffset`, and `preDefinedSeed` strategies, optional range checking, and an end-of-job summary. Modules call `ServiceHandle<SeedService>->getSeed()` from their ctor or `beginRun`. Essential for reproducibility across simulation, mixing, and reconstruction stages.

## Key contents
- `SeedService.hh` - service API, policy enum, fhicl docs in header
- `EngineId.hh`, `ArtState.hh` - engine identity and art-state guard helpers
- `SeedTest01_module.cc` plus `test/test*.fcl` - policy regression suite

## Inputs / Outputs
- **Consumes:** fcl `policy`, `baseSeed`, `maxUniqueEngines`, per-module offsets/seeds
- **Produces:** `SeedService` art service returning `long int` seeds registered with `art::RandomNumberGenerator`

## Example usage
```
services.SeedService : {
  policy           : "autoIncrement"
  baseSeed         : 0
  maxUniqueEngines : 20
}
```

## Related
- [[TimeoutService]]
