# CRVResponse

**Role:** CRV simulation chain: propagate scintillation photons, simulate SiPM response, build waveforms, and digitize to `CrvDigi`s.

## Overview
Converts `StepPointMC` energy depositions in CRV scintillator bars into realistic CRV digis via lookup tables of photon arrival times plus SiPM, amplifier and ADC models. The output `CrvDigi`s are the direct MC analogue of the DAQ digis consumed by `CRVReco`. Also provides MC-truth linking modules that associate coincidence clusters back to their generating particles, and a variety of test/analysis modules (single-counter, wideband, efficiency checks).

## Key contents
- `CrvStepsFromStepPointMCs_module` — collects `StepPointMC`s into per-bar `CrvStep`s.
- `CrvPhotonGenerator_module` (+ `MakeCrvPhotons`) — photon arrival times from lookup tables.
- `CrvSiPMChargeGenerator_module` (+ `MakeCrvSiPMCharges`) — SiPM pixel avalanches incl. crosstalk and dark counts.
- `CrvWaveformsGenerator_module` (+ `MakeCrvWaveforms`) — analog waveform shaping using `data/singlePEWaveform*.txt`.
- `CrvDigitizer_module` (+ `MakeCrvDigis`) — ADC digitization to produce `CrvDigi`s.
- `CrvCoincidenceClusterMatchMC_module`, `MakeCrvCoincidenceClusterMCAssns_module`, `CrvMCHelper` — MC truth matching.
- `CrvPlot_module`, `CRVTest_module`, `CrvWidebandTest_module` — diagnostics; `fcl/prolog_v12.fcl` plus extensive `test/` fcl suite.

## Inputs / Outputs
- **Consumes:** `StepPointMC`s in CRV volumes; `CosmicRayShield` geometry; `CRVCalib`/`CRVStatus`/`CRVPhotonYield`/`CRVOrdinal` proditions; DAQ timing conditions; single-PE waveform tables; photon lookup tables (external).
- **Produces:** `CrvStep`, `CrvPhotons`, `CrvSiPMCharges`, `CrvDigiMCCollection`, `CrvDigi`, `CrvCoincidenceClusterMCAssns`.

## Example usage
```
mu2e -c Offline/CRVResponse/test/CRVResponse.fcl -s stepPointMC.art -n 100
```

## Related
- [[CRVReco]]
- [[CRVConditions]]
- [[CosmicRayShieldGeom]]
- [[DAQConditions]]
- [[MCDataProducts]]
- [[Mu2eG4]]
