# Parallella Modern

A modern, lightweight Linux distribution for the **Parallella 16** (Zynq-7010 + 16-core Epiphany).

The goal is to revive the Parallella with a clean, maintainable, and user-friendly system that feels like a modern embedded Linux experience rather than the 2015-era images.

## Goals

- Minimal but usable desktop environment (XFCE preferred)
- Easy first-boot setup (hostname, root password, WiFi)
- Modern kernel and toolchain
- Strong Epiphany SDK integration with Python support
- Simple update mechanism
- Low resource requirements suitable for the board's hardware
- Support for specialized RISC-based LLM workloads (quantized inference, attention kernels, speculative decoding helpers, KV cache management)
- FPGA bitstream loading support

## Image Variants

We provide two main configurations:

| Variant   | Target Use Case                     | Desktop | Size   |
|-----------|-------------------------------------|---------|--------|
| Headless  | Servers, edge nodes, ML inference   | No      | Small  |
| Desktop   | Development, education, general use | XFCE    | Larger |

## Target Use Cases

- Edge / low-power parallel computing research
- Tiny ML inference experiments (especially quantized models)
- RISC-specific LLM components (attention scoring, draft models, speculative decoding)
- FPGA + Epiphany co-design experiments
- Educational platform for parallel RISC programming
- Lightweight desktop or headless development board

## Current Status

**Early development** — Repository structure and planning phase.

Planned features:
- Buildroot-based images (headless + desktop)
- First-boot configuration script (Ubuntu Server style)
- Easy WiFi setup
- Updated Epiphany toolchain + Python bindings
- Simple FPGA bitstream loader
- Simple over-the-air update system
- Example RISC-optimized LLM kernels

## Repository Structure

```
parallella-modern/
├── README.md
├── LICENSE
├── docs/                    # Documentation and plans
├── buildroot/
│   └── configs/             # Buildroot defconfigs (headless + desktop)
├── scripts/
│   ├── firstboot/           # First-boot installer
│   └── fpga/                # FPGA bitstream tools
├── examples/
│   └── ml/                  # Tiny model examples + RISC LLM kernels
└── .github/
```

## Contributing

This project is just getting started. Contributions, ideas, and feedback are welcome — especially in these areas:

- Buildroot configuration and package selection
- Epiphany programming and tooling improvements
- Small ML / parallel workloads and RISC-optimized LLM kernels
- FPGA integration
- Documentation and user experience

## License

MIT License — see [LICENSE](LICENSE) file.