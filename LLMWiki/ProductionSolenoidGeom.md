# ProductionSolenoidGeom

**Role:** Geometry description of the Production Solenoid (PS) and its immediate surroundings: enclosure, vacuum, external shielding, and HRS/heat-and-radiation shield.

## Overview
Holds data classes describing the PS cold mass/cryostat, the downstream PS enclosure, the PS vacuum volume, the bronze/tungsten HRS (`PSShield`), and the external concrete shielding. Populated by Makers in [[GeometryService]] from SimpleConfig and exposed to G4 construction and downstream consumers through `GeomHandle`.

## Key contents
- `ProductionSolenoid.hh` - PS cold mass / cryostat tubes and polycones.
- `PSEnclosure.hh` - downstream window and enclosure of the PS vacuum.
- `PSVacuum.hh` - PS vacuum volume description.
- `PSShield.hh` - layered heat and radiation shield (HRS).
- `PSExternalShielding.hh` - external concrete/steel shielding around the PS.

## Inputs / Outputs
- **Consumes:** SimpleConfig geometry parameters (via the PS Makers in [[GeometryService]]); [[GeomPrimitives]] shapes.
- **Produces:** PS geometry Detector objects served through [[GeometryService]]; consumed by G4 construction, [[BFieldGeom]] placement, and [[ProductionTargetGeom]] placement.

## Related
- [[GeometryService]]
- [[GeomPrimitives]]
- [[ProductionTargetGeom]]
- [[BeamlineGeom]]
- [[BFieldGeom]]
