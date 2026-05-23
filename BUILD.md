# Building Parallella Nemo

## Current Status (v1)

The Buildroot external tree is now in a working, buildable state.

**Known limitation**: Python3 and aggregator are disabled in the current defconfig due to toolchain compatibility issues with the Zynq configuration. A future update will resolve this.

## Quick Build

```bash
./build.sh
```

This will:
1. Clone Buildroot (shallow) if not present
2. Apply `defconfig-headless`
3. Build the image

## Packages Included

- etop
- firstboot
- explorer
- fpga-loader
- epiphany

## Output

Images will be in `../buildroot/output/images/`.