# CRVConfig

**Role:** Header-only fhicl `Config` structs describing the fcl stanzas accepted by CRV conditions providers.

## Overview
A small INTERFACE library that defines the `fhicl::Atom`/`Sequence` schemas for CRV proditions (`CRVCalib`, `CRVStatus`, `CRVPhotonYield`, `CRVOrdinal`). `CRVConditions` includes these configs so that fcl validation and documentation live in one place, separate from the provider implementations. No source files, no data products.

## Key contents
- `CRVCalibConfig.hh` — pedestal, pulse-height, pulse-area, time-offset universal values plus `useDb`/`verbose`.
- `CRVStatusConfig.hh` — status-flag override list and DB toggle.
- `CRVPhotonYieldConfig.hh` — MC photon-yield deviation options.
- `CRVOrdinalConfig.hh` — channel-map file path and DB toggle.

## Inputs / Outputs
- **Consumes:** nothing at runtime; header-only.
- **Produces:** C++ types used by `CRVConditions` `*Maker` constructors.

## Related
- [[CRVConditions]]
- [[DbTables]]
