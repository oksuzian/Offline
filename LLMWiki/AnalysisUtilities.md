# AnalysisUtilities

**Role:** ROOT/TMVA macros for training and calibrating track-quality (TrkQual) classifiers used downstream in reconstruction.

## Overview
This package is not an art library but a small collection of ROOT scripts that consume TrkAna ntuples produced by production jobs and train TMVA-based classifiers (notably the track-quality MVA). It lives in Offline so the training recipe and the reconstruction consumers share a single source of truth. Outputs (XML weights files) are registered through the MVA catalog and served via `AnalysisConfig` / the conditions database.

## Key contents
- `scripts/TrainTrkQual.C` - TMVA classifier training macro (based on the standard TMVA classification example)
- `scripts/RunTrainTrkQual.C` - driver wrapping `TrainTrkQual.C` for standard Mu2e training samples
- `scripts/CalibTrkQual.C`, `RunCalibTrkQual.C` - post-training calibration / diagnostics
- `CMakeLists.txt` - registers the scripts directory

## Inputs / Outputs
- **Consumes:** TrkAna ROOT ntuples (signal + background), TMVA libraries
- **Produces:** TMVA weights XML and calibration files consumed via the `MVACatalog`

## Example usage
```
root -l -b -q Offline/AnalysisUtilities/scripts/RunTrainTrkQual.C
```

## Related
- [[AnalysisConfig]]
- [[ParticleID]]
- [[Mu2eKinKal]]
