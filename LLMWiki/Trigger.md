# Trigger

**Role:** Offline representation of Mu2e's software trigger (HLT) paths: bookkeeping, prescaling, path read-back, and per-path diagnostics.

## Overview
Mu2e's trigger is a set of art filter paths (defined across `CaloFilters`, `TrkFilters`, `CRVFilters`, `CosmicReco`, etc.); this package is the framework-level glue that records which trigger paths fired, merges their per-path `TriggerInfo` objects, applies additional prescales, and provides analyzers for the final cut-flow. It is used both online-like (inside a triggered reco job) and offline to study trigger efficiency, rates, and path overlaps on simulation or real data.

## Key contents
- `src/MergeTriggerInfo_module.cc` — merges per-path `TriggerInfo` products into a single summary
- `src/TriggerInfoToCollections_module.cc` — unpacks trigger info back into flat collections for analysis
- `src/PrescaleEvent_module.cc` — configurable event prescaler used inside trigger paths
- `src/DigiFilter_module.cc` — digi-level pre-filter seed for trigger paths
- `src/ReadTriggerInfo_module.cc`, `ReadTriggerPath_module.cc` — analyzers producing per-path cut-flow histograms
- `src/EvalWeightedEventCounts_module.cc` — rate/efficiency bookkeeping with event weights
- `fcl/read_trig_paths.fcl` — driver for the trigger-path read-back analyzer

## Inputs / Outputs
- **Consumes:** art `TriggerResults`, per-path `TriggerInfo` products, `KalSeedCollection`, `CaloCluster`/`CrvCoincidence`, `ProtonBunchIntensity`
- **Produces:** merged `TriggerInfo` product, flat trigger collections, TFileService cut-flow histograms, prescale filter decisions

## Example usage
```
mu2e -c Offline/Trigger/fcl/read_trig_paths.fcl -s triggered.art
```

## Related
- [[CaloFilters]]
- [[TrkFilters]]
- [[CRVFilters]]
- [[Filters]]
- [[Lumi]]
- [[Validation]]
