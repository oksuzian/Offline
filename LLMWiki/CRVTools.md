# CRVTools

**Role:** Small user-facing CRV utilities, currently a digi/status ntuple dumper.

## Overview
Holds lightweight CRV analysis/debug tools that do not belong in the core reco or simulation libraries. At present the package contains only the `CrvDigiDump` analyzer used to flatten `CrvDigi` and CRV status collections into ROOT ntuples for quick inspection.

## Key contents
- `CrvDigiDump_module.cc` — art analyzer; writes CRV digi waveforms and status to ROOT trees.
- `fcl/crvDigiDump.fcl` — ready-to-run driver fcl.

## Inputs / Outputs
- **Consumes:** `CrvDigi` collection (default label `CrvDigi`); CRV status product.
- **Produces:** ROOT ntuples via `TFileService` (default `crvDigiDump.root`).

## Example usage
```
mu2e -c Offline/CRVTools/fcl/crvDigiDump.fcl -s input.art -n -1
```

## Related
- [[CRVReco]]
- [[CRVResponse]]
- [[Print]]
