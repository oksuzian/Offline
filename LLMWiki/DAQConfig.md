# DAQConfig

**Role:** fhiclcpp configuration schemas for DAQ proditions.

## Overview
DAQConfig is a header-only package holding the fhicl-validated struct for the `EventTiming` prodition. Keeping the schema separate avoids a dependency cycle between [[DAQConditions]] and modules that inject the configuration.

## Key contents
- `EventTimingConfig.hh` - schema for `verbose`, `useDb`, `TimeFromProtonsToDRMarker`, `OffSpillEventLength`

## Inputs / Outputs
- **Consumes:** nothing at runtime (header-only schema)
- **Produces:** validated config struct consumed by [[DAQConditions]] maker

## Related
- [[DAQConditions]], [[DAQ]]
- [[STMConfig]] - sibling config-schema pattern
