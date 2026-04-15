# MBSGeom

**Role:** Geometry of the Muon Beam Stop (MBS) located at the downstream end of the Detector Solenoid.

## Overview
The MBS absorbs muons and secondaries that exit the stopping target region so they do not re-enter the detector or experimental hall. This package describes its mother volume, stainless-steel pipe sections (BSTS), HDPE shields (SPBS, BSTC), and service access holes, following docdb-1351. The geometry is consumed by the Mu2eG4 MBS constructor and registered through [[GeometryService]].

## Key contents
- `MBS.hh` - top-level Muon Beam Stop geometry (mother + sub-volumes)
- `src/MBSMaker.cc` - builds from SimpleConfig
- Uses Tube and Polycone primitives from [[GeomPrimitives]]

## Inputs / Outputs
- **Consumes:** `Mu2eG4/geom/mbs*.txt` SimpleConfig parameters
- **Produces:** `MBS` detector object consumed by `constructMBS` in Mu2eG4

## Related
- [[DetectorSolenoidGeom]]
- [[StoppingTargetGeom]]
- [[MECOStyleProtonAbsorberGeom]]
- [[GeomPrimitives]]
