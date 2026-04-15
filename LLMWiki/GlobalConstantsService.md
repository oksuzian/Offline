# GlobalConstantsService

**Role:** art service that serves run-independent physics constants and the particle data list to all modules.

## Overview
Loads a `SimpleConfig` text file of globally valid constants at job start and builds on-demand `ConditionsEntity` objects (particle masses, physics parameters, mass cache). Consumers fetch entries through `GlobalConstantsHandle<ENTITY>`. Unlike [[ProditionsService]], values here are not time-dependent and do not flow from the conditions DB.

## Key contents
- `GlobalConstantsService.hh`, `GlobalConstantsHandle.hh` - service + typed accessor
- `ParticleData.hh`, `ParticleDataList.hh`, `unknownPDGIdName.hh` - PDG table
- `PhysicsParams.hh`, `MassCache.hh` - physics constants and mass memoization
- `data/globalConstants_01.txt`, `data/ParticleList.txt` - default input files

## Inputs / Outputs
- **Consumes:** `SimpleConfig` text inputs (`globalConstants_01.txt`, `ParticleList.txt`) and fcl overrides
- **Produces:** `GlobalConstantsService` art service delivering `PhysicsParams`, `ParticleDataList`, `MassCache`

## Example usage
```
services.GlobalConstantsService : {
  inputFile : "Offline/GlobalConstantsService/data/globalConstants_01.txt"
}
```

## Related
- [[GeometryService]]
- [[ProditionsService]]
