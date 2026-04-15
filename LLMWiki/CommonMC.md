# CommonMC

**Role:** Shared Monte Carlo utility modules and helpers used across simulation, mixing, and reconstruction-truth workflows.

## Overview
CommonMC collects framework modules and library code that manipulate generic MC data products (SimParticles, StepPointMCs, MCPrimary, SurfaceSteps) independent of any specific subsystem. It sits alongside the simulation flow, providing glue pieces like primary-truth finders, time-offset generators, and MC-to-reco matching helpers. The modules are consumed by fcl sequences that stitch [[EventGenerator]], [[Mu2eG4]], [[EventMixing]], and reconstruction into complete jobs.

## Key contents
- `src/FindMCPrimary_module.cc`, `NullMCPrimary_module.cc` - identify/label the primary SimParticle for an event
- `src/ProtonTimeOffset_module.cc`, `CosmicTimeOffset_module.cc`, `ProtonBunchTimeMCFromProtonBunchTime_module.cc` - MC bunch-time offset producers
- `src/MakeSurfaceSteps_module.cc`, `SurfaceStepDiag_module.cc` - synthesize and diagnose surface-crossing steps
- `src/SelectRecoMC_module.cc` - MC-truth filtering keyed to reconstructed objects
- `src/StoppedParticlesFinder_module.cc`, `SimParticleDaughterSelector_module.cc` - topology selectors on SimParticle trees
- `src/TrkMCTools.{hh,cc}` - library helpers linking tracker MC hits to truth

## Inputs / Outputs
- **Consumes:** SimParticleCollection, StepPointMCCollection, MCTrajectoryCollection, ProtonBunchTimeMC, RecoDataProducts, geometry/conditions via [[ProditionsService]]
- **Produces:** MCPrimary, EventWindowMarker, SurfaceStepCollection, time-offset products, diagnostic TTrees

## Example usage
```
physics.producers.FindMCPrimary: { module_type: FindMCPrimary }
```

## Related
- [[MCDataProducts]]
- [[EventGenerator]]
- [[Mu2eG4]]
- [[EventMixing]]
- [[Mu2eUtilities]]
