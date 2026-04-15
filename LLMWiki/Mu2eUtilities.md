# Mu2eUtilities

**Role:** Mu2e-aware helper library: physics spectra, track/geometry math, random utilities, and MC bookkeeping tools that know about Mu2e data products.

## Overview
Where [[GeneralUtilities]] is experiment-agnostic, Mu2eUtilities layers on top and pulls in Mu2e-specific knowledge: decay/capture spectra used by generators, helix and least-squares fit tools for pattern recognition, random-number utilities tied to the proton-pulse and art RNG, and helpers that walk `SimParticle`/`StepPointMC` collections. It is the go-to kitchen drawer for code that needs Mu2e physics or event-content awareness without pulling in a full subsystem library.

## Key contents
- Physics spectra: `CzarneckiSpectrum`, `ShankerWatanabeSpectrum`, `ConversionSpectrum`, `MuonCaptureSpectrum`, `PionCaptureSpectrum`, `BinnedSpectrum`.
- Fitting/geometry: `LsqSums2`, `LsqSums4`, `ParametricFit`, `TwoLinePCA`, `HelixTool`, `MedianCalculator`.
- MC helpers: `SimParticleParentGetter`, `SimParticleGetTau`, `compressSimParticleCollection`, `PhysicalVolumeMultiHelper`.
- Random / proton-pulse: `RandomUnitSphere`, `RandomLimitedExpo`, `ProtonPulseRandPDF`, `artURBG`, `ReSeedByEventID`.
- MVA & tools: `MVATools`, `ModuleHistToolBase`, `McUtilsToolBase`, `RootTreeSampler`.

## Inputs / Outputs
- **Consumes:** Mu2e data products (`SimParticle`, `StepPointMC`, `KalSeed`, etc.) and conditions from [[GlobalConstantsService]].
- **Produces:** `Offline::Mu2eUtilities` library linked broadly across reconstruction, MC, and analysis packages.

## Related
- [[GeneralUtilities]]
- [[MCDataProducts]]
- [[RecoDataProducts]]
- [[SeedService]]
- [[EventGenerator]]
- [[fcl]]
