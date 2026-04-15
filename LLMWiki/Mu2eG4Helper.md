# Mu2eG4Helper

**Role:** Small art service and utilities for bookkeeping Geant4 logical/physical volumes and objects whose lifetime must outlive a G4 run.

## Overview
Mu2eG4Helper provides the `Mu2eG4Helper` art service plus the `VolumeInfo` record struct and the `AntiLeakRegistry` - a registry that keeps long-lived Geant4 objects alive so that Geant4's ownership quirks do not cause leaks or dangling pointers. It is used throughout [[Mu2eG4]] geometry construction code to register logical/physical volume pairs and retrieve them by name across the many `construct*.cc` functions.

## Key contents
- `inc/Mu2eG4Helper.hh`, `src/Mu2eG4Helper_service.cc`, `src/Mu2eG4Helper.cc` - the art service
- `inc/VolumeInfo.hh`, `src/VolumeInfo.cc` - logical/physical volume record
- `inc/AntiLeakRegistry.hh`, `src/AntiLeakRegistry.cc` - registry of owned G4 objects

## Inputs / Outputs
- **Consumes:** calls from G4 construction code registering volumes; no fcl parameters of its own
- **Produces:** the `Mu2eG4Helper` service with `locateVolInfo`, `addVolInfo`, and an `AntiLeakRegistry` handle

## Related
- [[Mu2eG4]]
- [[GeometryService]]
