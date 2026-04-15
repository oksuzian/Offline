# bin

**Role:** Small collection of shell/ROOT driver scripts used by developers to perform common Offline housekeeping tasks.

## Overview
These are not build artifacts but hand-written helper executables shipped with the source tree. They cover package scaffolding, geometry inspection, fcl maintenance, and data-file lookup. They sit on top of an already-built Offline environment and are meant to be invoked directly from a shell after `setup_for_development`.

## Key contents
- `newPackage` - scaffold a new top-level Offline package directory.
- `overlapCheck.sh`, `overlapCheck.C`, `printOverlaps.sh` - drive GDML/Geant4 geometry overlap checks.
- `viewGeometry.C`, `gdmldiff`, `browse` - ROOT-based geometry browsing and GDML diffing.
- `check_bfield_grid.sh`, `findDataFiles.sh` - sanity-check calibration/B-field inputs and locate data files.
- `updateFCLFile.sh` - batch-edit fcl fragments.
- `addroot.sh`, `check_cmake.sh` - environment/build helpers.

## Inputs / Outputs
- **Consumes:** an initialized Offline environment (see [[ups]], [[scripts]]); for geometry scripts, GDML files produced by [[Mu2eG4]].
- **Produces:** console output, ROOT browser windows, new package skeletons, or edited files in place.

## Example usage
```shell
# Create a new package directory
Offline/bin/newPackage MyNewPackage

# Check geometry overlaps
Offline/bin/overlapCheck.sh mu2e.gdml
```

## Related
- [[scripts]]
- [[ups]]
- [[fcl]]
- [[Mu2eG4]]
