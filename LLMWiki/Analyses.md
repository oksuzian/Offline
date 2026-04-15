# Analyses

**Role:** Grab-bag of art analyzer / filter modules and fcl examples used for ad-hoc studies, debugging, and sub-detector-level checks of Mu2e data.

## Overview
This package is the historical catch-all for small analyzers that dump, print, or histogram Mu2e data products (SimParticles, StepPointMCs, VirtualDetector hits, straw digis, calo digis, BField maps, etc.). Most modules here are short, single-purpose tools used during MC production campaigns, detector studies, or bug hunts rather than part of the production reconstruction chain. New long-lived analysis code typically migrates into a detector-specific package; Analyses remains a staging ground.

## Key contents
- `src/ReadBack_module.cc`, `ReadVirtualDetector_module.cc`, `ReadStrawDigiReco_module.cc` — common read-back analyzers over MC + digis
- `src/SimParticle*`, `StepPointMC*Dumper_module.cc` — SimParticle / StepPointMC inspection and text/tree dumps
- `src/CaloCalib*`, `CaloDigiAna`, `CaloClusterCompare_module.cc` — calorimeter-level studies
- `src/BFieldPlotter_module.cc`, `GeomVis_module.cc`, `PrintTrackerGeom_module.cc` — geometry / field visualization
- `src/CORSIKAGenPlots_module.cc`, `CRYGenPlots_module.cc`, `CountPionDecays_module.cc` — generator checks
- `fcl/`, `test/` — dozens of runnable example fcl driving the above modules

## Inputs / Outputs
- **Consumes:** almost every data product (`MCDataProducts`, `RecoDataProducts`, `SimParticleCollection`, `StepPointMCCollection`, `StrawDigiCollection`, `CaloDigiCollection`, `GenParticleCollection`), geometry via `GeomHandle`, BField services
- **Produces:** TFileService histograms / ntuples, stdout dumps, occasional filter decisions (e.g. `FilterEmptyEvents_module.cc`, `CosmicFilter_module.cc`)

## Example usage
```
mu2e -c Offline/Analyses/test/eventLister.fcl -s input.art
```

## Related
- [[AnalysisUtilities]]
- [[AnalysisConfig]]
- [[Validation]]
- [[UtilityModules]]
- [[Print]]
- [[EventDisplay]]
