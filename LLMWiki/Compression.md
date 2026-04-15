# Compression

**Role:** Slim MC truth payload by dropping unobservable objects while preserving the Ptr network to the products that are kept.

## Overview
Because Mu2e MC products (SimParticle, StepPointMC, StrawGasStep, CaloShowerStep, CrvStep, MCTrajectory, ...) hold art::Ptrs into one another, naively dropping truth breaks references. This package provides coherent rewriters that re-map all Ptrs when compressing truth. Two flavors exist: `StepCompression` works on raw detector-step aggregates, while `DigiCompression` runs after digitization to keep only truth tied to the digis that survive. It is a key stage for producing mixed/overlay samples and analysis-sized outputs.

## Key contents
- `CompressDetStepMCs_module` — compresses StrawGasStep/CaloShowerStep/CrvStep/SurfaceStep collections pre-digi
- `CompressDigiMCs_module` — post-digi MC-truth compression tied to surviving StrawDigi/CaloDigi/CrvDigi
- `CompressDigiMCsCheck_module` — diagnostic check that Ptr networks remain valid
- `CompressionLevel` enum library — noCompression / simParticleCompression / fullCompression levels
- `fcl/prolog.fcl` — `DetStepCompression` presets (`noCompression`, `standardCompression`, `extraCompression`) and `DigiCompressionTags`

## Inputs / Outputs
- **Consumes:** [[MCDataProducts]] (SimParticleCollection, StepPointMC, StrawGasStep, CaloShowerStep, CrvStep, StrawDigiMC, ...), [[DataProducts]], generation-count configuration
- **Produces:** slimmed copies of the same [[MCDataProducts]] collections with remapped Ptrs

## Example usage
```
#include "Offline/Compression/fcl/prolog.fcl"
physics.producers.compressDigiMCs: {
  module_type : CompressDigiMCs
  @table::DetStepCompression.standardCompression
  @table::DigiCompressionTags
}
```

## Related
- [[MCDataProducts]]
- [[CommonMC]]
- [[EventMixing]]
- [[Mu2eG4]]
- [[Filters]]
