# ParticleID

**Role:** Likelihood-based electron/muon particle identification from tracker dE/dx and calorimeter E/p, applied to fitted Kalman tracks.

## Overview
ParticleID builds per-track log-likelihoods for the electron and muon hypotheses using reference templates (dE/dx vs path, E/p vs momentum, drift-time residuals, cross-section tables) that ship with the package under versioned `data/` subdirectories. The `ParticleID` producer attaches a PID log-likelihood-ratio object to each fitted track (`MergePatRec`/`MergePatRecDem`/`Dmm`), and a read-back analyzer is provided for studies. Different fit collections (downstream e-, downstream mu-) are supported via fhicl templates.

## Key contents
- `src/PIDLogL1D.cc`, `PIDLogLEp.cc`, `PIDLogLRatio.cc` — 1-D / E-over-p / ratio log-likelihood calculators
- `src/PIDUtilities.cc` — shared helpers for template I/O and interpolation
- `src/ParticleIDRead_module.cc` — analyzer for reading/plotting PID output
- `data/v5_7_9/pid_{ele,muo}_{dedx,dt,ep_vs_path,xdrds}.{tbl,rtbl}` — current template set (older v4_2_4 / v5_7_0 / v5_7_2 retained)
- `fcl/prolog.fcl` — standard producer templates: `ParticleID`, `ParticleIDDeM`, `ParticleIDDmuM`

## Inputs / Outputs
- **Consumes:** `KalSeedCollection` from `MergePatRec*`, calorimeter cluster/track matches, reference `.tbl`/`.rtbl` template files
- **Produces:** per-track PID log-likelihood-ratio data product

## Related
- [[Mu2eKinKal]]
- [[CalPatRec]]
- [[TrkPatRec]]
- [[AnalysisUtilities]]
- [[AnalysisConfig]]
