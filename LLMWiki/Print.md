# Print

**Role:** Diagnostic analyzer modules and companion fcl that dump Mu2e data products to stdout for debugging and quick inspection.

## Overview
Print provides a uniform family of `*Printer` classes - one per major data product (SimParticle, StepPointMC, CaloCluster, KalSeed, ComboHit, CRV coincidences, trigger results, etc.) - plus a `PrintModule` art analyzer that strings them together with per-product verbosity and cuts. Ready-to-run fcl files (`print.fcl`, `printKalSeed.fcl`, ...) let users dump any art event content without writing code. A small set of standalone executables (`artProductSizes`, `eventCount`, `deps`) round out the file-level diagnostics.

## Key contents
- `PrintModule` analyzer (`src/PrintModule_module.cc`) orchestrating all printers.
- Per-product printer classes in `inc/` / `src/` deriving from `ProductPrinter`.
- `fcl/` ready-to-run dumps: `print.fcl`, `printSimParticle.fcl`, `printKalSeed.fcl`, `printCaloCluster.fcl`, etc.
- Standalone CLI tools: `artProductSizes/`, `eventCount/`, `deps/`.

## Inputs / Outputs
- **Consumes:** art files containing Mu2e MC or reco data products.
- **Produces:** human-readable text on stdout; `artProductSizes` reports per-branch on-disk sizes.

## Example usage
```shell
mu2e -c Offline/Print/fcl/print.fcl -s input.art -n 10

artProductSizes input.art
eventCount input.art
```

## Related
- [[fcl]]
- [[MCDataProducts]]
- [[RecoDataProducts]]
- [[DataProducts]]
- [[Validation]]
