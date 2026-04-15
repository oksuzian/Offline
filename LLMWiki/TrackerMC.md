# TrackerMC

**Role:** Tracker digitization: turns Geant4 straw gas steps into realistic `StrawDigi` waveforms.

## Overview
TrackerMC simulates the full straw response: it selects/merges Geant4 `StrawGasStep`s, generates ion clusters along the track, propagates them to the wire, shapes the analog waveform, adds noise/crosstalk, and writes `StrawDigi` + MC-truth collections indistinguishable from real DAQ output. Its product is the entry point to the reco chain starting at [[TrkHitReco]].

## Key contents
- `MakeStrawGasSteps_module.cc`, `StationStepSelector_module.cc` — gas-step preparation
- `StrawDigisFromStrawGasSteps_module.cc` — main digitization module
- `PoissonTrackerNoise_module.cc` — random noise hit generator
- `MakeMCKalSeed_module.cc` — MC-truth "perfect" KalSeed for studies
- `StrawWaveform`, `AnalogWireSignal`, `TruncatedSinusoid`, `IonCluster`, `StrawCluster*` — analog-chain building blocks
- `StrawDigiBundle{,Collection}` — grouped digi container
- `TruncatedSinusoidTool_tool.cc`, `AnalogSignalShapeTool.hh` — pluggable shaping tools

## Inputs / Outputs
- **Consumes:** `StepPointMCCollection`/`StrawGasStepCollection` from Mu2eG4, `StrawResponse`, `StrawElectronics`, `StrawPhysics` ([[TrackerConditions]]), tracker geometry
- **Produces:** `StrawDigiCollection`, `StrawDigiADCWaveformCollection`, `StrawDigiMCCollection`

## Example usage
```
#include "Offline/TrackerMC/fcl/prolog.fcl"
physics.producers.makeSD : @local::TrackerMC.StrawDigisFromStrawGasSteps
```

## Related
- [[TrackerGeom]], [[TrackerConditions]] — geometry and response
- [[TrkHitReco]] — consumes the produced digis
