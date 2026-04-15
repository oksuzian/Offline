# GeneralUtilities

**Role:** Mu2e-agnostic C++ utility library of math, string, I/O, and small-data-structure helpers.

## Overview
GeneralUtilities collects generic building blocks that have no dependency on Mu2e data products or geometry: numerical helpers (safe sqrt, RMS, min/max, spline interpolation, digital filtering), geometric primitives (two-line PCA, line-point PCA, HepTransform), small MVA wrappers, enum-to-string plumbing, string/CSV parsing, binning, and parameter-set helpers. It is linked by nearly every other package in Offline and is deliberately kept free of art- and Geant4-specific types.

## Key contents
- Math/stats: `RMS`, `MinMax`, `SequenceStatistics`, `SplineInterpolation`, `DigitalFiltering`, `safeSqrt`, `polyAtan2` (in Mu2eUtilities).
- Geometry primitives: `HepTransform`, `LinePointPCA`, `LineSegmentPCA`, `TwoDPoint`, `OrientationResolver`.
- Containers/enums: `BitMap`, `EnumToStringSparse`, `MVAStruct`, `OwningPointerCollection`.
- Parsing/strings: `CsvReader`, `StringVec`, `splitLine`, `splitString`, `toHex`, `trimInPlace`.
- Binning & file utilities: `Binning`, `NUBinning`, `PathnameWithNextVersion`, `ParameterSetFromFile`, `ParseCLI`.

## Inputs / Outputs
- **Consumes:** N/A (pure utility library, depends only on standard C++/CLHEP).
- **Produces:** `Offline::GeneralUtilities` library used transitively by nearly every subsystem.

## Related
- [[Mu2eUtilities]]
- [[ConfigTools]]
- [[DataProducts]]
