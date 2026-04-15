# ProditionsService

**Role:** "Provider of Conditions" - art service delivering time-dependent conditions entities assembled from the DB and fcl.

## Overview
`ProditionsService` is the Mu2e runtime conditions framework. It owns one `ProditionsCache` per subsystem entity (tracker alignment, straw response, calorimeter DAQ map, CRV calibs, STM energy calib, event timing, TrkQual catalog, sim bookkeeping, ...) and builds each entity by combining fcl parameters with rows fetched through [[DbService]] keyed by IoV. Clients obtain a current, thread-safe snapshot via `ProditionsHandle<ENTITY>`. Most subsystem `*Conditions` folders in the repo are Proditions-based makers registered here.

## Key contents
- `ProditionsService.hh` - service + fhicl schema listing every registered entity
- `ProditionsHandle.hh` - typed, IoV-aware handle used by modules
- `src/ProditionsService.cc`, `ProditionsTest_module.cc` - registration and smoke test
- `fcl/prolog.fcl` - standard `Proditions` table wiring all subsystem prologs
- `test/proditionsTest.fcl` - reference job for validating entity loading

## Inputs / Outputs
- **Consumes:** [[DbService]] tables from [[DbTables]], per-entity fcl prologs from `AnalysisConditions`, `CRVConditions`, `CaloConditions`, `DAQConditions`, `STMConditions`, `SimulationConditions`, `TrackerConditions`
- **Produces:** `ProditionsService` art service and typed `ProditionsEntity` snapshots (`StrawResponse`, `AlignedTracker`, `CRVCalib`, `SimBookkeeper`, `TrkQualCatalog`, ...)

## Example usage
```
#include "Offline/ProditionsService/fcl/prolog.fcl"
services.ProditionsService : @local::Proditions
services.DbService         : @local::DbEmpty
```

## Related
- [[DbService]]
- [[DbTables]]
- [[AnalysisConditions]]
- [[SimulationConditions]]
