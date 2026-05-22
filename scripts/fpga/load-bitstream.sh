#!/bin/bash
# Simple FPGA bitstream loader for Parallella
# Usage: parallella-load-bitstream <bitstream.bit>

if [ $# -ne 1 ]; then
    echo "Usage: $0 <bitstream.bit>"
    exit 1
fi

BITSTREAM="$1"

if [ ! -f "$BITSTREAM" ]; then
    echo "Error: File not found: $BITSTREAM"
    exit 1
fi

echo "Loading bitstream: $BITSTREAM"

# Common locations for FPGA programming on Zynq
if [ -e /sys/class/fpga/fpga0/load ]; then
    cat "$BITSTREAM" > /sys/class/fpga/fpga0/load
elif [ -e /dev/xdevcfg ]; then
    cat "$BITSTREAM" > /dev/xdevcfg
else
    echo "FPGA programming interface not found."
    echo "You may need to load the appropriate kernel module."
    exit 1
fi

echo "Bitstream loaded successfully."