# Filters

**Role:** Generic, cross-subsystem art event-filter modules used to skim, prescale, and thin simulation and reconstruction streams.

## Overview
This is the central home for event-level filters that are not tied to a single detector (distinct from `CaloFilters`, `CRVFilters`, etc.). Modules here decide whether to keep an event, thin `StepPointMCCollection`s, prescale, enforce good-run status, or throttle beam/cosmic mixing. Filters run throughout the MC production chain — from post-G4 truth thinning to trigger-emulated reco skims — and most MC job configurations wire several of them together via `fcl/prolog.fcl`.

## Key contents
- Truth thinning: `FilterG4Out`, `CompressPhysicalVolumes`, `CompressStepPointMCs`, `StepPointFilter`, `SelectStepPointsByTime`, `StepPointsInDigis`
- StepPoint kinematic cuts: `FilterStepPointMomentum`, `FilterStepPointKinEnPDG`, `FilterStepPointPDG`, `FilterStepPoint{Position,Pz,Angle}VsTarget`, `FilterStepPointReflection`, `GenParticleMomFilter`
- Prescale / bookkeeping: `RandomPrescaleFilter`, `FixedFilter`, `GoodRunFilter`, `TriggerResultsFilter`, `SelectEvents`, `WeightSamplingFilter`
- Subsystem-step/digi filters: `StrawGasStepFilter`, `StrawDigiMCFilter`, `TrackerStepPointFilter`, `CaloPileupDtsFilter`, `CaloDtsClusterFilter`, `CaloShowerSimFilter`, `EMFBoxHitsFilter`, `EMFPixel{Hits,Sim}Filter`
- Beam/cosmic & reco skims: `BunchIntensityFilter`, `CosmicMixingFilter`, `DetectorStepFilter`, `RecoMomFilter`, `TrkQualFilter`, `ParticleCodeFilter`, `VetoIncorrectHits`, `KilledEventFilter`, `FilterCosmicsStage1`, `FilterStatusG4`

## Inputs / Outputs
- **Consumes:** [[MCDataProducts]], [[RecoDataProducts]], [[DataProducts]], ProtonBunchIntensity, TriggerResults, conditions (TrackerConditions, DbService good-run lists)
- **Produces:** art filter decisions (pass/fail), optionally reduced `StepPointMCCollection`, `PhysicalVolumeInfo*`, and thinned MC collections

## Example usage
```
physics.filters.stepMomFilter : @local::FilterStepPointMomentum
physics.trigger_paths : [ path_with_filter ]
```

## Related
- [[Compression]]
- [[MCDataProducts]]
- [[RecoDataProducts]]
- [[CommonMC]]
- [[CaloFilters]]
- [[CRVFilters]]
- [[TrkFilters]]
- [[EventMixing]]
