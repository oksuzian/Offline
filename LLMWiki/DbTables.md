# DbTables

**Role:** Row/schema definitions for every calibration or validity table stored in the Mu2e conditions database.

## Overview
Each header declares a `DbTable` subclass whose rows mirror one conditions-DB table (tracker alignment, calorimeter calibs, CRV channels, STM pedestals, validity/IoV metadata, etc.). These classes are the type-safe bridge between the CSV blobs returned by [[DbService]] and the Proditions makers in subsystem `*Conditions` folders. No art modules live here - it is a pure library.

## Key contents
- `DbTable.hh`, `DbTableFactory.hh`, `DbTableCollection.hh` - base class + registry
- `DbIoV.hh`, `DbSet.hh`, `DbCache.hh`, `DbValCache.hh`, `DbVersion.hh` - IoV, versioning, and in-memory cache machinery
- Tracker tables: `TrkAlignStraw`, `TrkAlignPanel`, `TrkDelay*`, `TrkPanelMap`, `TrkPreamp*`, `TrkThreshold*`
- Calorimeter tables: `Cal*EnergyCalib`, `Cal*TimeCalib`, `CalChannels`, `CalChannelStatus`
- CRV / STM / Sim / MVA tables: `CRVBadChan`, `CRVSiPM`, `STMPedestals`, `SimEfficiencies2`, `MVAToolDb`
- `Val*.hh` - validation/metadata tables (IoVs, groups, purposes, versions)
- `TstCalib[1-3].hh`, `TstAdhoc1.hh` - test fixtures

## Inputs / Outputs
- **Consumes:** CSV text returned from the conditions DB by [[DbService]]
- **Produces:** Concrete `DbTable`-derived row containers consumed by [[ProditionsService]] entity makers and subsystem `*Conditions` folders

## Related
- [[DbService]]
- [[ProditionsService]]
