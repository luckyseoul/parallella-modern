# Parallella Modern

A modern, lightweight Linux distribution for the **Parallella 16** (Zynq-7010 + 16-core Epiphany).

The goal is to revive the Parallella with a clean, maintainable, and user-friendly system that feels like a modern embedded Linux experience rather than the 2015-era images.

## Goals

- Minimal but usable desktop environment (XFCE preferred)
- Easy first-boot setup (hostname, root password, WiFi)
- Modern kernel and toolchain
- Good Epiphany SDK integration with Python support
- Simple update mechanism
- Low resource requirements suitable for the board's hardware

## Target Use Cases

- Edge / low-power parallel computing research
- Tiny ML inference experiments
- Educational platform for parallel RISC programming
- Lightweight desktop or headless development board

## Current Status

**Early development** — Repository structure and planning phase.

Planned features:
- Buildroot-based image
- XFCE desktop (or very lightweight alternative)
- First-boot configuration script
- Easy WiFi setup
- Updated Epiphany toolchain + Python bindings
- Simple over-the-air update system

## Repository Structure

```
parallella-modern/
├── README.md
├── LICENSE
├── docs/                    # Documentation and plans
├── buildroot/
│   └── configs/             # Buildroot defconfig
├── scripts/                 # First-boot, WiFi, update tools
├── examples/
│   └── ml/                  # Tiny model examples
└── .github/
```

## Contributing

This project is just getting started. Contributions, ideas, and feedback are welcome — especially in these areas:

- Buildroot configuration and package selection
- Epiphany programming and tooling improvements
- Small ML / parallel workloads
- Documentation and user experience

## License

MIT License — see [LICENSE](LICENSE) file.