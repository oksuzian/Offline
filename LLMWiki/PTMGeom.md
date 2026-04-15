# PTMGeom

**Role:** Geometry description of the Production Target Monitor (PTM), a pair of proportional wire chambers upstream of the production target used to profile the incoming proton beam.

## Overview
The PTM consists of two proportional wire chambers (near and far) on a support stand, packaged as a "head" positioned at a chosen location/rotation in the Mu2e frame. This folder provides the data classes for each subpiece. A corresponding Maker in [[GeometryService]] reads SimpleConfig and returns a fully populated `PTM` via `GeomHandle`.

## Key contents
- `PTM.hh` - top-level assembly: stand + head (or directly two PWCs), origin and rotation in Mu2e.
- `PTMHead.hh` - holder combining the two PWCs with their separation and mother-volume margin.
- `PTMPWC.hh` - single proportional wire chamber geometry.
- `PTMStand.hh` - mechanical support stand.

## Inputs / Outputs
- **Consumes:** SimpleConfig parameters (via the Maker in [[GeometryService]]); [[GeomPrimitives]] shapes.
- **Produces:** `PTM` Detector served through [[GeometryService]]; consumed by G4 construction and PTM-specific digitization/analysis.

## Related
- [[GeometryService]]
- [[GeomPrimitives]]
- [[ProductionTargetGeom]]
- [[BeamlineGeom]]
