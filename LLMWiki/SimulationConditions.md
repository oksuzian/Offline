# SimulationConditions

**Role:** Proditions entity holding simulation bookkeeping (stage efficiencies) used to normalize staged MC.

## Overview
Provides the `SimBookkeeper` Proditions entity, a name-to-efficiency map populated either from fcl or from the `SimEfficiencies2` DB table. Downstream reweighting code queries it to correctly combine multi-stage productions (e.g. POT to muon-beam to muon-stop fractions) when computing absolute normalizations.

## Key contents
- `SimBookkeeper.hh` - `ProditionsEntity` storing `map<string,double>` of tagged efficiencies
- `SimBookkeeperCache.hh` - Proditions cache keyed on IoV
- `SimBookkeeperMaker.hh` / `.cc` - builds entity from fcl or DB rows
- `fcl/prolog.fcl` - default `SimBookkeeper` stanza with baseline efficiencies

## Inputs / Outputs
- **Consumes:** `SimEfficiencies2` rows via [[DbService]]/[[DbTables]], `SimBookkeeperConfig` from [[SimulationConfig]]
- **Produces:** `SimBookkeeper` Proditions entity served by [[ProditionsService]]

## Example usage
```
#include "Offline/SimulationConditions/fcl/prolog.fcl"
services.ProditionsService.simbookkeeper : @local::SimBookkeeper
```

## Related
- [[ProditionsService]]
- [[SimulationConfig]]
- [[DbTables]]
