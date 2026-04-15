# Mu2eG4

**Role:** The full Geant4 integration for Mu2e - world construction, physics lists, sensitive detectors, actions, and the art producer that runs G4 per event.

## Overview
Mu2eG4 is the simulation workhorse and the largest folder in the G4/Simulation cluster. It wraps Geant4 inside art: the `Mu2eG4_module` (single-threaded) and `Mu2eG4MT_module` (multi-threaded) drive event-by-event tracking, consuming GenParticles from [[EventGenerator]] and emitting SimParticles, StepPointMCs, trajectories, and volume/calorimeter showers. The package owns world/geometry construction (`Mu2eWorld`, `construct*.cc` for DS/PS/CRV/STM/calorimeter/tracker/extmon/shielding), custom physics constructors and biasing, user actions (stacking, stepping, tracking, event, run), sensitive detectors for every subsystem, field managers, and MT master/worker run managers. Extensive fcl in `fcl/` and study configs in `g4study/` cover standard staged simulation, GDML dumps, surface checks, and dedicated G4 studies.

## Key contents
- `src/Mu2eG4_module.cc`, `Mu2eG4MT_module.cc`, `Mu2eG4MTRunManager.cc`, `Mu2eG4WorkerRunManager.cc`, `MTMasterThread.cc` - art producers and MT run managers
- `src/Mu2eWorld.cc`, `Mu2eStudyWorld.cc`, `WorldMaker.cc`, `ConstructMaterials.cc`, `construct*.cc` - geometry construction
- `src/Mu2eG4*PhysicsConstructor.cc`, `Mu2eG4BiasedRDPhysics.cc`, `Mu2eG4MinimalModularPhysicsList.cc` - physics lists
- `src/Mu2eG4{Stacking,Stepping,Tracking,Event,Run,Master}Action.cc`, `Mu2eG4Cuts.cc`, `Mu2eG4TrajectoryControl.cc` - user actions and cuts
- `src/*SD.cc` (StrawSD, CaloCrystalSD, CRVSD, ExtMonFNALPixelSD, ...) - sensitive detectors
- `fcl/g4test_0*.fcl`, `fcl/g4test_stage[01]*.fcl`, `fcl/gdmldump*.fcl`, `fcl/surfaceCheck.fcl`, `g4study/*.fcl` - standard job configs

## Inputs / Outputs
- **Consumes:** GenParticleCollection / StageParticleCollection from [[EventGenerator]], geometry via [[GeometryService]], B-field via [[BFieldGeom]], materials conditions, Mu2eG4 fcl parameters, [[SeedService]]
- **Produces:** SimParticleCollection, StepPointMCCollection (tracker, calorimeter, CRV, virtual detectors, extmon, STM, PTM), CaloShowerStepCollection, MCTrajectoryCollection, PhysicalVolumeInfoMultiCollection, status products; optional GDML files

## Example usage
```
mu2e -c Offline/Mu2eG4/fcl/g4test_03MT.fcl -n 100
```

## Related
- [[EventGenerator]]
- [[EventMixing]]
- [[CommonMC]]
- [[Mu2eG4Helper]]
- [[Mu2eInterfaces]]
- [[MCDataProducts]]
- [[GeometryService]]
- [[BFieldGeom]]
