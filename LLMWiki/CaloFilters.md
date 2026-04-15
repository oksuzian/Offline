# CaloFilters

**Role:** Trigger- and analysis-level filter modules using calorimeter clusters.

## Overview
Implements `art::EDFilter` modules that select events with calorimeter activity matching Conversion-Electron (CE) signatures — via simple cluster-counter cuts, BDT likelihoods, or neural-network scores. Used both in the online [[Trigger]] paths and in offline skims. Also provides a cosmic-calibration selector.

## Key contents
- `CaloClusterCounterFilter_module` — multiplicity/energy cut on `CaloClusterCollection`
- `CaloLikelihood_module` — BDT-based CE vs. background likelihood (weights under `data/`)
- `FilterEcalMixedTrigger_module`, `FilterEcalMVATrigger_module` — trigger-path BDT filters
- `CaloNNEval_module` + `FilterEcalNNTrigger_module` — evaluate calo NN score and cut
- `CaloCosmicCalib_module` — cosmic-ray selection for calibration runs
- `data/*.weights.xml` — shipped TMVA weight files (BDT + NN)

## Inputs / Outputs
- **Consumes:** `CaloClusterCollection`, `CaloHitCollection`
- **Produces:** filter decision (event pass/fail), optional `TFileService` diagnostic histograms

## Related
- [[CaloCluster]] — upstream data product
- [[CaloDiag]] — trains the NN weight files
- [[Trigger]], [[TrkFilters]] — sibling filter subsystems
