# ProductionTargetGeom

**Role:** Geometry description of the Mu2e production target (tungsten "Hayman" target inside the Production Solenoid).

## Overview
Defines the `ProductionTarget` data class holding the target rod/support geometry, placement, and rotation in the Mu2e coordinate system. It is a minimal, single-class package - construction logic lives in the corresponding Maker in [[GeometryService]], which reads SimpleConfig and hands the resulting object out via `GeomHandle<ProductionTarget>` for G4 construction and analyses.

## Key contents
- `ProductionTarget.hh` / `ProductionTarget.cc` - target geometry (position, rotation, rod/fin dimensions, supports).

## Inputs / Outputs
- **Consumes:** SimpleConfig parameters (via the Maker in [[GeometryService]]); [[GeomPrimitives]] shapes.
- **Produces:** `ProductionTarget` Detector served through [[GeometryService]]; consumed by G4 construction, primary proton generators, and [[PTMGeom]] positioning references.

## Related
- [[GeometryService]]
- [[GeomPrimitives]]
- [[ProductionSolenoidGeom]]
- [[PTMGeom]]
- [[ProtonBeamDumpGeom]]
