# Validation

**Role:** Reference-histogram package that generates and compares standard distributions for every major Mu2e data product, powering the CI validation workflow.

## Overview
Validation centralizes the "one histogram set per data product" pattern used by Mu2e's nightly / PR validation. The `Validation` art analyzer loops over the event and, for each collection type it recognizes, delegates to a small `Val<ProductName>` class that books and fills a canonical set of plots. The companion ROOT-side `TValCompare` / `TValHist*` infrastructure and the standalone `valCompare` executable then compare a new run's validation.root against a reference and flag statistically significant changes. This is what CI uses to detect unintended reconstruction / simulation drift.

## Key contents
- `src/Validation_module.cc` — analyzer that dispatches every known data product to its `Val*` filler
- `src/Val<ProductName>.cc` — per-product histogram bundles (e.g. `ValKalSeed`, `ValStrawDigi`, `ValCaloCluster`, `ValCrvCoincidenceCluster`, `ValHelixSeed`, `ValSimParticle`, `ValStepPointMC`, `ValTriggerResults`, ...)
- `root/TValCompare.cc`, `TValHist{,E,H,P,2}.cc`, `TValPar.cc` — ROOT-side comparison classes with statistical tests
- `src/valCompare_main.cc` — standalone `valCompare` CLI for comparing two validation.root files
- `fcl/val.fcl` — canonical validation job (process name `validation1`, output `validation.root`)

## Inputs / Outputs
- **Consumes:** virtually every Mu2e data product (MC, reco, trigger, CRV, calo, tracker, STM, proton-bunch); driven by `RootInput`
- **Produces:** `validation.root` with hundreds of reference histograms; CLI comparison reports (pass/fail + per-hist statistics)

## Example usage
```
mu2e -c Offline/Validation/fcl/val.fcl -s reco.art
valCompare new/validation.root ref/validation.root
```

## Related
- [[Analyses]]
- [[Trigger]]
- [[RecoDataProducts]]
- [[MCDataProducts]]
- [[Print]]
