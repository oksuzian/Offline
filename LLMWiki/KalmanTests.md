# KalmanTests

**Role:** Legacy ROOT macros and validation scripts for the original BaBar-Kalman tracking era.

## Overview
KalmanTests holds standalone ROOT/C macros used historically to study the BTrk-based Kalman fit (DIO spectra, resolution, cosmic checks, panel/straw studies, flash cuts). The folder no longer ships production C++ code; it is retained as a reference and for reproducing older plots. Current tracking validation lives alongside [[Mu2eKinKal]] and [[TrkReco]].

## Key contents
- `test/mu2e.C`, `test/do_mu2e.C`, `test/mu2e_scan.C` — top-level driver macros
- `test/DIO*.{C,h}`, `test/CMspectrum.C`, `test/dio.C`, `test/dioacc.C` — decay-in-orbit spectrum/acceptance studies
- `test/Cosmics.C`, `test/Reflect.C`, `test/TestFlash.C` — cosmic and flash-background studies
- `test/EStraw.C`, `test/Panel.C`, `test/ResConv.C`, `test/T2d.C` — straw/panel and resolution macros

## Inputs / Outputs
- **Consumes:** legacy ROOT trees/ntuples produced by older tracking jobs
- **Produces:** plots/histograms for validation notes

## Related
- [[BTrkLegacy]] — companion legacy types
- [[Mu2eKinKal]] — modern fitter superseding this test suite
- [[TrkReco]]
