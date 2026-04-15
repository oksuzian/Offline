# DAQConditions

**Role:** Proditions for DAQ/event-timing parameters shared across subsystem unpackers.

## Overview
DAQConditions provides the `EventTiming` Prodition, which encodes the time offset between the proton pulse and the DR (data-request) marker, along with the off-spill event length in clock counts. These numbers are required to align digi timestamps across the tracker, calorimeter, CRV, and STM when decoding DTC/artdaq fragments, and to define off-spill windows for cosmic and calibration streams.

## Key contents
- `EventTiming.hh/.cc` - Prodition entity carrying `timeFromProtonsToDRMarker` and `offSpillLength`
- `EventTimingMaker.hh/.cc` - builder from fcl (or DB when `useDb : true`)
- `fcl/prolog.fcl` - default values (200 ns proton-to-DR offset, 4000-ct off-spill length)

## Inputs / Outputs
- **Consumes:** fcl stanza `EventTiming` (see [[DAQConfig]]); optional DbTables when `useDb`
- **Produces:** `EventTiming` Prodition consumed by [[DAQ]] unpackers and downstream reco

## Related
- [[DAQ]], [[DAQConfig]]
- [[ProditionsService]], [[DbService]]
