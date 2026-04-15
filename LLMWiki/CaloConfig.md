# CaloConfig

**Role:** Header-only fhicl `ConfigTools` structs that parameterise the calorimeter conditions providers.

## Overview
Defines the C++ config schemas (`fhicl::Table`-style) used by [[CaloConditions]] makers to read their fcl parameters in a type-safe way. Installed as an INTERFACE library — no compiled sources.

## Key contents
- `CalCalibConfig.hh` — config for `CalCalibMaker` (DB vs. file, ADC-to-MeV, time offset)
- `CaloDAQMapConfig.hh` — config for `CaloDAQMapMaker` (file spec, verbosity, DB flag)

## Inputs / Outputs
- **Consumes:** fhicl parameter sets
- **Produces:** compile-time config structs used by [[CaloConditions]]

## Related
- [[CaloConditions]]
- [[ConfigTools]]
