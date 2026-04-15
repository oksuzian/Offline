# SimulationConfig

**Role:** fhicl schema types consumed by [[SimulationConditions]] Proditions makers.

## Overview
A minimal header-only package that declares validated fhicl structs (currently `SimBookkeeperConfig` and `SimStageEffConfig`) describing how simulation-stage efficiencies are configured. Keeping the schema separate from the Proditions entity avoids circular includes between `ProditionsService` and `SimulationConditions`.

## Key contents
- `SimBookkeeperConfig.hh` - `verbose`, `useDb`, sequence of `SimStageEffConfig { tag, eff }` entries

## Inputs / Outputs
- **Consumes:** nothing at runtime; headers only
- **Produces:** fhicl validated types used in [[ProditionsService]] and [[SimulationConditions]] `Maker` code

## Related
- [[SimulationConditions]]
- [[ProditionsService]]
