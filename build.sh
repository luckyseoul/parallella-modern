#!/bin/bash
# Build script for Parallella Nemo

set -e

BR2_EXTERNAL=$(pwd)/external/parallella
DEFCONFIG=$BR2_EXTERNAL/defconfig

echo "Building Parallella Nemo..."

# This assumes Buildroot is cloned at ../buildroot
if [ ! -d "../buildroot" ]; then
    echo "Error: Buildroot not found at ../buildroot"
    echo "Please clone Buildroot first:"
    echo "  git clone https://gitlab.com/buildroot.org/buildroot.git ../buildroot"
    exit 1
fi

make -C ../buildroot BR2_EXTERNAL=$BR2_EXTERNAL defconfig BR2_DEFCONFIG=$DEFCONFIG
make -C ../buildroot BR2_EXTERNAL=$BR2_EXTERNAL

echo "Build complete."