# GeometryService

**Role:** art service that builds and distributes the run-time Mu2e detector geometry assembled from all `*Geom` subsystems.

## Overview
On `preBeginRun` the service parses `inputFile` (and `bFieldFile`) through `SimpleConfig`, then invokes a suite of `*Maker` classes to construct the concrete geometry objects for every subsystem - tracker, calorimeter, CRS, solenoids, target, MBS, ExtMonFNAL, STM, PTM, shielding, Mu2e hall, virtual detectors, and the Geant4 world. Client modules retrieve typed detector handles through `GeomHandle<DET>`. This service is the canonical geometry source for both reconstruction and `Mu2eG4` simulation.

## Key contents
- `GeometryService.hh`, `GeomHandle.hh`, `DetectorSystem.hh` - service + typed handle API
- `G4GeometryOptions.hh`, `WorldG4Maker.hh`, `Mu2eHallMaker.hh` - G4 world assembly
- `TrackerMaker.cc`, `DiskCalorimeterMaker.cc`, `CosmicRayShieldMaker.cc`, `BFieldManagerMaker.cc`, ... - per-subsystem builders
- `Mu2eEnvelope.hh`, `Mu2eCoordTransform.hh`, `DUSAFMu2eConverter.hh` - coordinate/envelope helpers

## Inputs / Outputs
- **Consumes:** `SimpleConfig` geometry text files (`inputFile`, `bFieldFile`), raw parameters from `*Geom` folders
- **Produces:** `GeometryService` art service providing `GeomHandle<Tracker>`, `GeomHandle<DiskCalorimeter>`, `WorldG4`, `BFieldManager`, etc.

## Example usage
```
services.GeometryService : {
  inputFile  : "Offline/Mu2eG4/geom/geom_common.txt"
  bFieldFile : "Offline/Mu2eG4/geom/bfgeom_reco_v01.txt"
  simulatedDetector : { tool_type : "Mu2e" }
}
```

## Related
- [[GlobalConstantsService]]
- [[ProditionsService]]
