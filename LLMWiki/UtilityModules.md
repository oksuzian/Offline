# UtilityModules

**Role:** Small, general-purpose art modules that manipulate existing data products or stand in as no-ops in a path.

## Overview
Developer-facing helpers for shaping art pipelines rather than doing new physics. Typical uses: dummy-out a producer without editing the path (so module labels, products, and random-seed counts remain consistent), pre-select stopped particles for downstream mixing, or massage track `StepPointMC` products for secondary mixing workflows.

## Key contents
- `src/NullProducer_module.cc` — no-op producer; optionally allocates random engines to preserve seed layout
- `src/RecoNullProducer_module.cc` — reco-side equivalent no-op producer
- `src/StopSelection_module.cc` — filter/producer selecting stopped particles (used for POT mixing inputs)
- `src/ModifyTrackSPM_module.cc`, `ReadTrackSPM_module.cc` — modify/read tracker `StepPointMC` collections (SPM) for resampling/mixing chains
- `test/modifyTrackSPM*.fcl`, `readTrackSPM*.fcl` — conv / detmix / flate workflow examples

## Inputs / Outputs
- **Consumes:** `StepPointMCCollection` (tracker), `SimParticleCollection`; seed counts via `SeedService`
- **Produces:** replacement `StepPointMCCollection`s, empty placeholder products, filter decisions

## Example usage
```
mu2e -c Offline/UtilityModules/test/modifyTrackSPM_conv.fcl -s input.art
```

## Related
- [[CommonMC]]
- [[EventMixing]]
- [[Compression]]
- [[SeedService]]
