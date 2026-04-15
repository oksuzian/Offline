# CaloDiag

**Role:** Diagnostic and MC-truth analyzers plus NN training pipeline for the calorimeter.

## Overview
Collection of `art::EDAnalyzer` modules producing ROOT histograms and ntuples to monitor calorimeter digi, hit, cluster, and MC performance. Also hosts a TMVA-based neutral-vs-charged cluster NN (`CaloNNDiag` for evaluation, `CaloNNTrain` for training), whose outputs feed the `CaloNNEval`/`FilterEcalNNTrigger` modules in [[CaloFilters]].

## Key contents
- `CaloExample_module` — reference analyzer: dumps hit/cluster/MC content to a TTree
- `CaloClusterCheck_module` — cluster-level sanity histograms
- `CaloMCInspector_module` — step-point / digi MC truth inspection
- `CaloNeutron_module` — neutron background studies
- `CaloNNDiag_module` / `CaloNNTrain_module` — TMVA cluster-NN diagnostic + training
- `test/check*plots.C`, `test/TMVACaloNN.C` — ROOT macros for the above

## Inputs / Outputs
- **Consumes:** `CaloDigi`, `CaloHit`, `CaloCluster`, `CaloHitTruthMatch`, `CaloClusterTruthMatch`, virtual-detector MC
- **Produces:** `TFileService` histograms/TTrees, trained TMVA weight files

## Related
- [[CaloReco]], [[CaloCluster]], [[CaloMC]] — source data products
- [[CaloFilters]] — deploys the trained NN
