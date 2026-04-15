# fcl

**Role:** Top-level shared fcl fragments providing common service, producer, and message-facility configurations for Mu2e jobs.

## Overview
This directory holds the repository-wide fhicl "prolog" snippets that virtually every Mu2e job `#include`s. It centralizes definitions for the art message service, random-number seed policies, standard services (Geometry, GlobalConstants, Conditions), and shared producer fragments, so that individual job fcl files can compose them instead of redefining them. Think of it as the small shared-header layer of the fcl ecosystem.

## Key contents
- `standardServices.fcl` - bundles Geometry, GlobalConstants, DbService, Proditions, SeedService.
- `standardProducers.fcl` - canonical producer module configurations.
- `standardInputs.fcl` - common input-source definitions.
- `minimalMessageService.fcl`, `messageService.fcl`, `standardMessageDestinations.fcl` - message-facility presets.
- `TrkCaloDt.fcl` - shared tracker-calorimeter timing fragment.

## Inputs / Outputs
- **Consumes:** prolog fragments from subsystem `*/fcl/prolog.fcl` files.
- **Produces:** fhicl prolog symbols that downstream job fcl files reference via `@local::...`.

## Example usage
```fcl
#include "Offline/fcl/standardServices.fcl"
#include "Offline/fcl/standardProducers.fcl"

services : @local::Services.Reco
```

## Related
- [[ConfigTools]]
- [[GeometryService]]
- [[SeedService]]
- [[DbService]]
- [[Print]]
