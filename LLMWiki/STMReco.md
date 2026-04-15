# STMReco

**Role:** Reconstruction chain from STM waveform digis to calibrated energy hits.

## Overview
STMReco processes HPGe and LaBr3 waveform digis through zero suppression, moving-window deconvolution (MWD), and hit making to yield `STMHit` energy spectra. The same modules run on both Monte Carlo digis from [[STMMC]] and real data digis unpacked from DTC fragments by [[DAQ]]. Diagnostic plotters and a test-beam variant of the chain are included.

## Key contents
- `STMZeroSuppression_module.cc` - amplitude-threshold zero suppression on waveforms
- `STMMovingWindowDeconvolution_module.cc` - MWD trapezoidal filter (tau/M/L)
- `MakeSTMHits_module.cc` - MWD digis to calibrated `STMHit`s
- `STMAnalyzeDigis_module.cc`, `PlotSTM{EnergySpectrum,MWDSpectrum,WaveformDigis}_module.cc`
- `fcl/{zeroSuppression,mwd,makeSTMHits,plotSTM*}.fcl` (+ `*_testbeam.fcl` variants)
- `fcl/prolog.fcl` - HPGe/LaBr ZS and MWD parameters

## Inputs / Outputs
- **Consumes:** `STMWaveformDigiCollection` from [[STMMC]] or [[DAQ]] (`STMWaveformDigisFromFragments`), `STMEnergyCalib` from [[STMConditions]]
- **Produces:** zero-suppressed waveform digis, `STMMWDDigiCollection`, `STMHitCollection`, diagnostic histograms

## Example usage
```
mu2e -c Offline/STMReco/fcl/zeroSuppression.fcl -s input.art
mu2e -c Offline/STMReco/fcl/mwd.fcl
mu2e -c Offline/STMReco/fcl/makeSTMHits.fcl
```

## Related
- [[STMMC]], [[STMConditions]], [[STMGeom]]
- [[DAQ]] - provides `STMWaveformDigisFromFragments` for real-data input
- [[RecoDataProducts]] - `STMHit`, `STMWaveformDigi`, `STMMWDDigi`
