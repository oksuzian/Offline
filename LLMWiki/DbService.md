# DbService

**Role:** art service that connects to the Mu2e conditions database and delivers calibration tables by IoV.

## Overview
`DbService` is the runtime gateway to the Mu2e conditions database (`mu2e_conditions_prd` and friends). It wraps a `DbEngine` that resolves a configured `purpose/version` into a set of `DbTable` payloads, manages a memory-limited cache, and hands out rows to clients via `DbHandle<T>`. It underlies [[ProditionsService]] and the various per-subsystem `*Conditions` makers, and also provides command-line tools for DB inspection.

## Key contents
- `DbService.hh`, `DbEngine.hh`, `DbReader.hh`, `DbSql.hh` - service + DB I/O
- `DbHandle.hh` - typed accessor used by clients to pull a table for current IoV
- `DbTool`, `EpicsTool`, `GrlTool`, `OpenTool`, `RunTool`, `DbValTool` - CLI binaries (`dbTool`, etc.)
- `data/create.sql`, `data/connections.txt` - DB schema and endpoint map
- `fcl/prolog.fcl` - `DbEmpty` stanza for no-DB running

## Inputs / Outputs
- **Consumes:** PostgreSQL conditions DB, `purpose`/`version` fcl parameters, optional `textFile` overrides
- **Produces:** `DbService` art service, `DbHandle<T>` table access, populated `DbTable` caches consumed by [[ProditionsService]]

## Example usage
```
services.DbService : { purpose : "MDC2020_best" version : "v1_3_0" dbName : "mu2e_conditions_prd" }
```
CLI: `dbTool print-table --name TrkAlignStraw --purpose PRODUCTION --version v1_0_0`

## Related
- [[DbTables]]
- [[ProditionsService]]
- [[GlobalConstantsService]]
