# Building Parallella Nemo

## Requirements

- Buildroot (recommended to clone at `../buildroot`)
- Host tools: make, gcc, etc.

## Quick Build

```bash
./build.sh
```

This will:
1. Configure Buildroot with the Parallella Nemo defconfig
2. Build the full image

## Manual Build

```bash
make -C ../buildroot BR2_EXTERNAL=$(pwd)/external/parallella \
    defconfig BR2_DEFCONFIG=$(pwd)/external/parallella/defconfig

make -C ../buildroot BR2_EXTERNAL=$(pwd)/external/parallella
```

## Output

The resulting image will be in `../buildroot/output/images/`.