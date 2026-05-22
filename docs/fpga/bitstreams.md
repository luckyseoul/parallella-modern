# FPGA Bitstream Support

The Parallella board includes a Zynq FPGA. This project provides basic support for loading custom bitstreams.

## Loading a Bitstream

```bash
parallella-load-bitstream my_design.bit
```

## Notes

- Bitstreams are usually generated with Xilinx Vivado or the older PlanAhead tools.
- The script currently supports the most common interfaces (`/sys/class/fpga` and `/dev/xdevcfg`).
- For advanced use cases, you may need to load additional kernel modules.

## Future Work

- Better error handling
- Support for multiple FPGA regions
- Integration with the Epiphany runtime (some bitstreams expose Epiphany interfaces)