# CaloVisualizer

**Role:** ROOT-based 2D visualisation of calorimeter disks.

## Overview
Small utility library that extends `TH2Poly` into `THMu2eCaloDisk`, a histogram class whose bins match the physical crystal layout of a calorimeter disk. Useful for quick-look plots of hit/cluster energy and time in analysis macros. Includes a ROOT dictionary so the class can be read from art output / `TFile`.

## Key contents
- `THMu2eCaloDisk` — `TH2Poly` subclass with per-crystal bins
- `src/classes.h`, `src/classes_def.xml` — ROOT dictionary registration

## Inputs / Outputs
- **Consumes:** crystal index + value arrays (from user analysis code)
- **Produces:** fillable ROOT histograms suitable for `TCanvas` drawing or PDF export

## Related
- [[CalorimeterGeom]] — defines the crystal layout
- [[EventDisplay]] — interactive 3D display sibling
- [[CaloDiag]] — typical client of these histograms
