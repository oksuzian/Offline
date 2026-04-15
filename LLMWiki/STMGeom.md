# STMGeom

**Role:** Geometric description of the Stopping Target Monitor (STM) detector system and its shielding.

## Overview
STMGeom defines the classes that describe the downstream Stopping Target Monitor: the HPGe and LaBr3 gamma detectors, collimators (FOV and SSC), permanent magnet, transport/shield pipes, support tables, absorber, and the multi-sided shielding assemblies. These classes are populated by `STMMaker` (in GeometryService) from SimpleConfig and exposed via the top-level `STM` detector object. They provide the geometric truth consumed by Mu2eG4, visualization, and downstream reconstruction coordinates.

## Key contents
- `STM.hh` - aggregate detector holding pointers to all STM sub-components
- `HPGeDetector.hh`, `LaBrDetector.hh`, `GeDetector.hh` - gamma detector crystals
- `STMCollimator.hh`, `PermanentMagnet.hh`, `TransportPipe.hh`, `ShieldPipe.hh` - beamline elements
- `STM_SSC.hh`, `SSCSupport.hh`, `STM_Absorber.hh` - Spot Size Collimator assembly and absorber
- `{Front,Back,Left,Right,Top,Bottom,Inner,Electronic}Shielding.hh` - shielding volumes
- `STMDownstreamEnvelope.hh`, `SupportTable.hh` - envelope and support infrastructure

## Inputs / Outputs
- **Consumes:** SimpleConfig geometry parameters via `STMMaker` (GeometryService)
- **Produces:** `STM` detector handle for Mu2eG4 construction, visualization, and reco

## Related
- [[STMMC]] - simulates energy deposits in these volumes
- [[STMConditions]] - per-channel calibrations indexed against this geometry
- [[STMReco]] - reconstruction against HPGe/LaBr channels defined here
- [[BeamlineGeom]], [[GeometryService]]
