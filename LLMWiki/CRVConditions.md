# CRVConditions

**Role:** Proditions providers for CRV calibrations, channel mapping, photon-yield deviations, and channel status flags.

## Overview
Supplies time-dependent CRV conditions to simulation and reconstruction through the `ProditionsService`. Each provider wraps a `DbTable` (or fcl override / text file) and caches the resolved per-channel constants (pedestals, pulse height/area, time offsets, PE deviations, dead-channel flags, DAQ ordinal mapping). Upstream modules in `CRVResponse` and `CRVReco` pull these via `ProditionsHandle<CRVCalib>` etc.

## Key contents
- `CRVCalib` / `CRVCalibMaker` / `CRVCalibCache` — per-channel pedestals, pulse-height and pulse-area calibrations, time offsets.
- `CRVStatus` / `CRVStatusMaker` — channel status flags (e.g. ignore/dead).
- `CRVPhotonYield` / `CRVPhotonYieldMaker` — per-channel photon yield deviations for MC.
- `CRVOrdinal` / `CRVOrdinalMaker` — ROC/FEB/channel <-> offline bar index mapping (`CRVROC`).
- `CRVDigitizationPeriod`, `CRVADCRange`, `CRVCalibPar` — shared small value types.
- `data/` — default text tables (`nominal`, `extracted`, `run1a_v01`, wideband test-stand variants, ...); `fcl/prolog.fcl` — provider prolog.

## Inputs / Outputs
- **Consumes:** `DbService` / `DbTables` rows when `useDb:true`; otherwise text files under `CRVConditions/data/`; `CosmicRayShieldGeom` for channel enumeration.
- **Produces:** Proditions entities `CRVCalib`, `CRVStatus`, `CRVPhotonYield`, `CRVOrdinal` (no art products).

## Example usage
```
#include "Offline/CRVConditions/fcl/prolog.fcl"
services.ProditionsService.crvCalib       : @local::CRVCalib
services.ProditionsService.crvStatus      : @local::CRVStatus
services.ProditionsService.crvPhotonYield : @local::CRVPhotonYield
services.ProditionsService.crvOrdinal     : @local::CRVOrdinal
```

## Related
- [[CRVConfig]]
- [[CRVReco]]
- [[CRVResponse]]
- [[DbService]]
- [[DbTables]]
- [[ProditionsService]]
