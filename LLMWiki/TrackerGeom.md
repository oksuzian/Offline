# TrackerGeom

**Role:** Persistent geometry description of the Mu2e straw tracker (planes, panels, straws, supports).

## Overview
TrackerGeom defines the data classes that represent the straw tracker's hierarchical geometry — `Tracker` → `Plane` → `Panel` → `Straw` — together with support structures and G4 helper info. The geometry is built by `GeometryService` at job start and then consumed everywhere: digitization, hit reco, pattern recognition, Kalman fitting, and event display. Alignment is layered on top via `AlignedTracker` in [[TrackerConditions]].

## Key contents
- `Tracker.{hh,cc}` — top-level tracker geometry
- `Plane.{hh,cc}`, `Panel.{hh,cc}`, `Straw.{hh,cc}` — hierarchy
- `StrawProperties.hh` — per-straw material/dimensional constants
- `SupportStructure.{hh,cc}`, `SupportModel.{hh,cc}`, `Support.hh` — mechanical supports
- `Manifold.{hh,cc}`, `ManifoldId.hh`, `PanelEB.hh` — electronics-board/manifold geometry
- `TrackerG4Info.hh` — companion info used when building the G4 representation

## Inputs / Outputs
- **Consumes:** `GeometryService` config (simple config/fhicl)
- **Produces:** `Tracker` object and child classes accessed via `GeomHandle<Tracker>`

## Related
- [[TrackerConditions]] — alignment and status on top of this geometry
- [[TrackerMC]] — digitization using straw positions
- [[TrkHitReco]], [[Mu2eKinKal]] — downstream geometry consumers
- [[KinKalGeom]] — analytic surface wrapper for fitting
