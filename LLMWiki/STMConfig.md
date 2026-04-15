# STMConfig

**Role:** fhiclcpp configuration schemas (Config structs) for STM proditions.

## Overview
STMConfig holds the `fhicl::Table`-style struct describing the STM energy-calibration stanza. Keeping the schema in its own package avoids circular dependencies between the Prodition implementation ([[STMConditions]]) and client modules, and lets validation run at fcl-parse time.

## Key contents
- `STMEnergyCalibConfig.hh` - fhicl schema for `STMEnergyCalib` (verbose, useDb, pedestals, samplingFrequencies)

## Inputs / Outputs
- **Consumes:** nothing at runtime (header-only schema)
- **Produces:** validated configuration struct used by [[STMConditions]] maker

## Related
- [[STMConditions]] - the Prodition that consumes this config
- [[DAQConfig]] - sibling pattern for DAQ proditions
