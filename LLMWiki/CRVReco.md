# CRVReco

**Role:** CRV reconstruction: turn `CrvDigi` waveforms into pulses, calibration constants, and coincidence clusters used for the cosmic-ray veto.

## Overview
Runs after CRV digitization (real data from the DAQ or MC from `CRVResponse`). It fits ADC pulses to extract time, height, area and PE counts, builds per-channel pedestal and calibration histograms, and searches for multi-layer coincidences that form the veto decision. Also hosts DQM, FPGA-rate, timing, wideband, and channel-map utilities.

## Key contents
- `CrvRecoPulsesFinder_module` (+ `MakeCrvRecoPulses`) — fits CRV digi waveforms to a log-normal pulse and produces `CrvRecoPulse`s.
- `CrvCoincidenceFinder_module` — clusters PE-weighted pulses across layers into `CrvCoincidenceCluster`s (the veto primitive).
- `CrvPedestalFinder_module` / `CrvCalibration_module` — build pedestal and gain/time calibration tables for the DB.
- `CrvDQMcollector_module`, `CrvFPGArate_module`, `CrvTimingStudies_module`, `CrvWidebandTriggerFilter_module`, `PrintCrvChannelMap_module` — monitoring / diagnostics.
- `CrvHelper` — shared geometry/channel lookup helpers; `fcl/prolog_v12.fcl` — canonical module parameter set.

## Inputs / Outputs
- **Consumes:** `CrvDigi` collection; `CRVCalib`, `CRVStatus`, `CRVOrdinal` proditions; `CosmicRayShield` geometry.
- **Produces:** `CrvRecoPulse`, `CrvCoincidenceCluster` data products; ROOT trees/histograms (pedestals, calibration, DQM, FPGA rates).

## Example usage
```
mu2e -c Offline/CRVReco/test/reco_wideband1module.fcl -s input.art -n 100
```

## Related
- [[CRVResponse]]
- [[CRVConditions]]
- [[CRVFilters]]
- [[CosmicRayShieldGeom]]
- [[RecoDataProducts]]
