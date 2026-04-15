# CRVFilters

**Role:** art filter modules that select events based on CRV reconstruction products.

## Overview
Minimal package containing trigger / skim filters keyed on CRV coincidence clusters. Currently a single filter is provided; it inspects `CrvCoincidenceCluster` collections and sets `TriggerInfo` for downstream trigger paths or output selection.

## Key contents
- `CrvCoincidenceClusterFilter_module.cc` — EDFilter that accepts events based on the presence/properties of `CrvCoincidenceCluster`s from `CrvCoincidenceClusterFinder`.

## Inputs / Outputs
- **Consumes:** `CrvCoincidenceCluster` collection (default label `CrvCoincidenceClusterFinder`); calorimeter geometry handles.
- **Produces:** filter decision; `TriggerInfo` when used on a trigger path.

## Related
- [[CRVReco]]
- [[Filters]]
- [[CaloFilters]]
- [[TrkFilters]]
