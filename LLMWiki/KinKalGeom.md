# KinKalGeom

**Role:** KinKal-compatible analytic surface descriptions of Mu2e subsystems used for track extrapolation and intersection.

## Overview
KinKalGeom provides lightweight geometric surface objects (cylinders, disks, planes) representing the tracker, detector solenoid, stopping target, and CRV, in the form expected by the external KinKal fitting library. These surfaces let [[Mu2eKinKal]] extrapolate fitted trajectories to physics-relevant boundaries without pulling in the full Geant-style geometry.

## Key contents
- `Tracker.{hh,cc}` — inner/outer tracker envelope surfaces
- `DetectorSolenoid.{hh,cc}` — DS-region cylinders/disks for extrapolation
- `StoppingTarget.{hh,cc}` — stopping-target foil surfaces
- `CRV.{hh,cc}`, `TestCRV.{hh,cc}` — CRV reference surfaces
- `SurfaceMap.{hh,cc}` — named registry mapping surface IDs to concrete surfaces

## Inputs / Outputs
- **Consumes:** `GeometryService` (tracker, DS, target, CRV geometry)
- **Produces:** `SurfaceMap` / surface objects used by extrapolation tools

## Related
- [[Mu2eKinKal]] — primary consumer (ExtrapolateToZ, ExtrapolateIPA, ExtrapolateST, ExtrapolateTCRV)
- [[TrackerGeom]] — tracker detail geometry
- [[CRVReco]]
