# STMMC

**Role:** Monte Carlo truth handling, digitization, resampling, and mixing for the Stopping Target Monitor.

## Overview
STMMC bridges Geant4 `StepPointMC` output at STM virtual detectors to realistic digitized waveforms used by reconstruction. It resamples and shifts VD101 steps into the HPGe/LaBr apertures, mixes beam backgrounds (one-batch, two-batch, target stops) at the appropriate POT rates, generates HPGe waveforms from step points, concatenates microspill waveforms, and produces analysis trees for efficiency and validation studies.

## Key contents
- `STMResamplingProducer_module.cc`, `STMResamplingFilter_module.cc` - resample VD101 steps
- `ShiftVirtualDetectorStepPointMCs_module.cc` - translate VD steps to HPGe/LaBr apertures
- `HPGeWaveformsFromStepPointMCs_module.cc` - step-to-waveform digitization
- `ConcatenateDigitizedWaveforms_module.cc`, `ConcatenationFilter_module.cc` - stitch microspills
- `HPGeTree_module.cc`, `MWDTree_module.cc`, `VirtualDetectorTree_module.cc` - TTree analyzers
- `DetectorEfficiency_module.cc`, `CountMixedEvents_module.cc`, `ValidateConsecutiveEventIDs_module.cc`

## Inputs / Outputs
- **Consumes:** `StepPointMCCollection` from `g4run:virtualdetector` (VD101, 88-90), mixed beam samples, [[STMGeom]] positions, fcl (`STMMC/fcl/prolog.fcl`)
- **Produces:** `STMWaveformDigiCollection` (DigiHPGe, DigiLaBr), concatenated waveforms, MC TTrees

## Example usage
```
mu2e -c Offline/STMMC/fcl/HPGeReco.fcl -s input.art
mu2e -c Offline/STMMC/fcl/Mix.fcl
```

## Related
- [[STMGeom]], [[STMConditions]] - geometry and calibration inputs
- [[STMReco]] - downstream consumer of digitized waveforms
- [[EventMixing]], [[CommonMC]], [[MCDataProducts]]
