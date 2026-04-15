# ups

**Role:** UPS (Fermilab's Unix Product Support) packaging glue that lets Offline participate in the Fermilab `cetmodules` / `mrb` / `spack` build ecosystem.

## Overview
This directory contains the shell-agnostic setup entry points and the `product_deps` manifest that declare Offline as a UPS product, list its dependencies (art, Geant4, ROOT, CLHEP, ...) and their qualifiers, and bootstrap a developer environment. Generated originally by `cetmodules`, these files are what `setup Offline` and `setup_for_development` consume at Fermilab-style sites.

## Key contents
- `product_deps` - declares product name, version, dependencies, and qualifier matrix.
- `setup_for_development` - shell-agnostic script sourced to initialize a developer environment from a source checkout.
- `setup_deps` - sets up just the declared dependencies (no Offline itself).

## Inputs / Outputs
- **Consumes:** a UPS/`cetmodules` environment (externals products on `PRODUCTS`).
- **Produces:** environment variables (`MU2E_BASE_RELEASE`, `MU2E_SEARCH_PATH`, `PATH`, `LD_LIBRARY_PATH`, compiler/qualifier selections) suitable for building and running Offline.

## Example usage
```shell
source /cvmfs/mu2e.opensciencegrid.org/setupmu2e-art.sh
cd Offline
source ups/setup_for_development -p
```

## Related
- [[scripts]]
- [[bin]]
- [[boost_fix]]
