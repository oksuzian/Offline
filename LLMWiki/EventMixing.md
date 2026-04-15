# EventMixing

**Role:** Mixes pile-up background frames (beam, cosmic, neutrons) into signal events and weights them by proton-bunch intensity.

## Overview
EventMixing sits between [[Mu2eG4]] and reconstruction in the Mu2e MC data flow. It overlays pre-simulated background events onto the current event at the detector-step or digit level, drawing samples according to a configurable ProtonBunchIntensity distribution. The package provides the core `Mu2eProductMixer` plus modules for frame-level and digit-level mixing, intensity generators (flat, log-normal), and selection tools that prune background StepPoints before they reach downstream stages.

## Key contents
- `src/Mu2eProductMixer.cc` (`inc/Mu2eProductMixer.hh`) - core mixing engine for Mu2e data products
- `src/MixBackgroundFrames_module.cc`, `MixDigis_module.cc`, `ResamplingMixer_module.cc` - art mixing filters
- `src/ProtonBunchIntensityFlat_module.cc`, `ProtonBunchIntensityLogNormal_module.cc` - PBI sampling
- `src/MixingFilter_module.cc` - accept/reject after mixing
- `src/*DetectorStepSelectionTool_tool.cc`, `PseudoCylindricalVolumeLookupTool_tool.cc` - art tools for step-level selection by volume/process
- `fcl/testVolumeMixing.fcl`, `test/mixProducer_01.fcl` - reference configurations

## Inputs / Outputs
- **Consumes:** secondary input files (background frames/digits), GenParticle/SimParticle/StepPointMC/CaloShower/StrawDigi products, ProtonBunchIntensity distributions, geometry volumes
- **Produces:** mixed SimParticleCollection, StepPointMC, CaloShowerStep, StrawDigi/CrvDigi collections, EventIDSequence, ProtonBunchIntensity per event

## Example usage
```
mu2e -c Offline/EventMixing/test/mixProducer_01.fcl -s sig.art -S bkg.lst
```

## Related
- [[Mu2eG4]]
- [[CommonMC]]
- [[EventGenerator]]
- [[MCDataProducts]]
- [[SeedService]]
