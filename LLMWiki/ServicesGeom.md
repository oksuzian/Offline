# ServicesGeom

**Role:** Geometry of service infrastructure (piping, electronic racks) in the detector hall.

## Overview
Describes non-detector services that must be modeled for shielding/background simulations: cryogenic and utility pipes (nested G4Tubs components) and electronic equipment racks. Details follow docdb #4678. Objects are registered with [[GeometryService]] and placed by Mu2eG4 alongside the hall and external shielding.

## Key contents
- `Pipe.hh` - nested-component pipes (PipeMaker)
- `ElectronicRack.hh` - racks of detector electronics
- Makers build from SimpleConfig; lightweight, no G4 dependency

## Inputs / Outputs
- **Consumes:** `Mu2eG4/geom/services*.txt`, pipe/rack SimpleConfig files
- **Produces:** `Pipe`, `ElectronicRack` detector objects

## Related
- [[Mu2eHallGeom]]
- [[ExternalShieldingGeom]]
- [[DetectorSolenoidGeom]]
- [[GeomPrimitives]]
