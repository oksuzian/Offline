# AnalysisConditions

**Role:** Proditions entities and MVA weight catalogs used by analysis-level quality selectors (e.g. TrkQual).

## Overview
Holds Proditions-backed catalogs of trained MVA classifiers (notably `TrkQual`) and the XML weight files they load. Downstream analysis/reco modules obtain the current MVA training set as a conditions object rather than hard-coding file paths, so calibrations can evolve by IoV.

## Key contents
- `MVACatalog.hh`, `MVACatalogCache.hh`, `MVACatalogMaker.hh` - generic Proditions catalog template
- `TrkQualCatalog.hh`, `TrkQualCatalogCache.hh` - TrkQual specialization
- `weights/TrkQual*.weights.xml` - serialized TMVA trainings (both charges)
- `fcl/prolog.fcl` - default `TrkQualCatalog` config referencing weight files

## Inputs / Outputs
- **Consumes:** `AnaTrkQualDb` / `MVAToolDb` rows via [[DbService]], TMVA XML weight files, fcl overrides
- **Produces:** `TrkQualCatalog` and related `MVACatalog<T>` Proditions entities for analysis modules

## Example usage
```
#include "Offline/AnalysisConditions/fcl/prolog.fcl"
services.ProditionsService.trkQualCatalog : @local::TrkQualCatalog
```

## Related
- [[ProditionsService]]
- [[DbService]]
- [[DbTables]]
