# BFieldTest

**Role:** Test / diagnostic art modules that sample the Mu2e magnetic field for validation and symmetry checks.

## Overview
This is a test utility, not a geometry description. It provides two art analyzers that query [[BFieldGeom]] through [[GeometryService]]: `BFieldTest` performs user-configured z-scans and writes `x y z Bx By Bz` text files for plotting; `BFieldSymmetry` compares field values at symmetric points and fills ROOT histograms/trees. Reference CSV field samples ship with the package for regression tests.

## Key contents
- `BFieldTest_module.cc` - multi-scan analyzer producing `<name>.txt` files readable by gnuplot.
- `BFieldSymmetry_module.cc` - symmetry check analyzer using `art_root_io::TFileService`.
- `test/BFieldTest.fcl`, `test/BFieldSymmetry.fcl` - example configurations.
- `test/Mau10_800mm_long.csv`, `test/bfield_rand_csv.txt` - reference field samples.

## Inputs / Outputs
- **Consumes:** `BFieldManager` from [[GeometryService]]; scan parameter sets from FHiCL; optional reference CSVs.
- **Produces:** per-scan `.txt` files, ROOT histograms/trees via TFileService.

## Example usage
```
mu2e -c Offline/BFieldTest/test/BFieldTest.fcl
```

## Related
- [[BFieldGeom]]
- [[GeometryService]]
