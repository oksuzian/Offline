# EventGenerator

**Role:** Produces primary particles (GenParticles) for all Mu2e simulation modes - signal, background, cosmics, calibration, and resampling of upstream stages.

## Overview
This is the first stage of the Mu2e MC data flow, feeding [[Mu2eG4]]. It houses framework modules and art tools that implement physics-driven primary generators (DIO, RMC, pion capture, Michel, muon capture products, cosmic rays) and utility guns (particle gun, primary proton gun, calo calibration). It also supports resampling previously simulated particles from ROOT/G4beamline/ASCII files to chain multi-stage simulations. Spectrum tables and default configuration fragments are shipped in `data/` and `defaultConfigs/`.

## Key contents
- `src/EventGenerator_module.cc`, `src/PrimaryProtonGun_module.cc`, `src/ParticleGun.cc` - top-level generators
- `src/CosmicCRY.cc`, `src/CosmicDYB.cc`, `src/CosmicFromTH2.cc`, `CORSIKAEventGenerator_module.cc`, `CRYEventGenerator_module.cc` - cosmic generators
- `src/DIOGenerator_tool.cc`, `RMCGenerator_tool.cc`, `Mu2eXGenerator_tool.cc`, `MuCap*Generator_tool.cc` - physics art tools
- `src/From{G4BLFile,SimParticleCompact,StepPointMCs,AsciiMomentumAndPosition}_module.cc` - multi-stage resamplers
- `src/PiCaptureEffects.cc`, `GammaConv*_module.cc`, `PBIWeight_module.cc` - physics effect modules
- `data/*.tbl`, `data/*.txt` - Czarnecki/Szafron/Heeck spectra, stopped-muon tables, neutron/photon spectra

## Inputs / Outputs
- **Consumes:** fcl generator configs, spectrum tables from `data/`, upstream SimParticle/StepPointMC/G4beamline files (for resamplers), ProtonBunchIntensity, geometry, [[SeedService]]
- **Produces:** GenParticleCollection, StageParticleCollection, GenEventCount, event weights, diagnostic histograms

## Example usage
```
physics.producers.generate: {
  module_type: EventGenerator
  inputfile: "Offline/EventGenerator/defaultConfigs/particleGun.txt"
}
```

## Related
- [[Mu2eG4]]
- [[CommonMC]]
- [[EventMixing]]
- [[MCDataProducts]]
- [[Mu2eUtilities]]
- [[SeedService]]
