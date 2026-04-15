# Blinding

**Role:** Hooks that enforce Mu2e's signal-region blinding policy on tracks and digis during analysis of sensitive datasets.

## Overview
Mu2e blinds the conversion-electron signal region until the analysis is unblinded by collaboration decision. This package provides the modules and tools that implement that policy: prescaling reconstructed tracks (KalSeeds) based on their kinematics, encrypting/decrypting blinded quantities, and perturbing digi timing so that the raw signal-region content cannot be trivially reconstructed from a protected file. The actual blinding cuts and keys are driven by fcl + tools; the physics-sensitive numeric bounds are kept out of this folder.

## Key contents
- `src/KalSeedFunctionalPrescale_module.cc` + `KalSeedPrescaleTool` — art Tools that prescale KalSeeds by momentum, quasi-impact parameter, tracker-exit azimuth, etc.
- `src/BigNumberProducer_module.cc`, `BigNumberChecker_module.cc`, `BigNumber.{hh,cc}` — arbitrary-precision integer product used for Goldwasser-Micali cryptography
- `src/GoldwasserMicaliEncrypter_module.cc`, `GoldwasserMicaliDecrypter_module.cc`, `GMPRoutines.{hh,cc}` — probabilistic public-key encryption of blinded bits
- `src/DisplaceDigiTimes_module.cc`, `MergeDigis_module.cc`, `TrackDigiExtractor_module.cc` — digi-level blinding / unblinding and selection

## Inputs / Outputs
- **Consumes:** `KalSeedCollection`, `StrawDigiCollection`, `CaloDigiCollection`, fcl-driven prescale lookup tables
- **Produces:** prescaled/blinded versions of the same collections, `BigNumber` product carrying encrypted quantities

## Related
- [[Mu2eKinKal]]
- [[TrkFilters]]
- [[Compression]]
- [[RecoDataProducts]]
