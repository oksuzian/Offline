# CosmicRayShieldGeom

**Role:** Geometric description of the Cosmic Ray Shield (CRS/CRV) detector: scintillator shields, modules, layers, bars and support structures.

## Overview
Provides the in-memory geometry objects for Mu2e's Cosmic Ray Veto, built by the `GeometryService` and consumed by every downstream CRV simulation, digitization, and reconstruction module. The hierarchy is `CosmicRayShield -> CRSScintillatorShield -> CRSScintillatorModule -> CRSScintillatorLayer -> CRSScintillatorBar`, with auxiliary descriptions for FEB boxes, aluminum sheets, absorber layers, and support steel. Index types (`CRSScintillatorBarIndex`, `...BarId`, `...LayerId`, `...ModuleId`, `...ShieldId`) make the hierarchy addressable from data products and conditions.

## Key contents
- `CosmicRayShield` — top-level detector object held by the geometry service; vends shields, modules, layers and bars.
- `CRSScintillatorShield` / `CRSScintillatorModule` / `CRSScintillatorLayer` / `CRSScintillatorBar` — hierarchical geometry classes.
- `CRSScintillatorBarDetail` — shared bar dimensions and material properties.
- `CRSScintillatorBarId`, `CRSScintillatorLayerId`, `CRSScintillatorModuleId`, `CRSScintillatorShieldId` — index/ID types used everywhere in CRV code.
- `CRSFEB`, `CRSAluminumSheet`, `CRSAbsorberLayer`, `CRSSupportStructure` — passive/auxiliary elements.

## Inputs / Outputs
- **Consumes:** `SimpleConfig` geometry files via `CosmicRayShieldMaker` (lives in `GeometryService`); `DataProducts` for bar indices.
- **Produces:** The `CosmicRayShield` detector object accessible through `GeomHandle<CosmicRayShield>`; no art data products.

## Related
- [[CRVResponse]]
- [[CRVReco]]
- [[CRVConditions]]
- [[GeometryService]]
- [[Mu2eG4]]
