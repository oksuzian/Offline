# ExternalShieldingGeom

**Role:** Geometry of the external (room-scale) shielding blocks and cryostat saddles around TS/DS.

## Overview
Describes concrete and steel shielding pieces built mostly as extruded solids, plus the saddles that support the solenoid cryostats. These are room-level shielding elements distinct from the in-cryostat DS shielding; they surround the transport and detector solenoids and fill the experimental hall. Details follow docdb #4678.

## Key contents
- `ExtShieldUpstream.hh` - upstream external shielding blocks
- `ExtShieldDownstream.hh` - downstream external shielding blocks
- `Saddle.hh` - cryostat support saddles (extrusions)
- Makers build objects from SimpleConfig; consumed by Mu2eG4 `constructExternalShielding`

## Inputs / Outputs
- **Consumes:** `Mu2eG4/geom/extshield*.txt`, saddle configs (SimpleConfig)
- **Produces:** `ExtShieldUpstream`, `ExtShieldDownstream`, `Saddle` detector objects in [[GeometryService]]

## Related
- [[GeomPrimitives]]
- [[DetectorSolenoidGeom]]
- [[Mu2eHallGeom]]
- [[ServicesGeom]]
