# Parallella Modern

A modern, user-friendly Linux distribution for the **Parallella 16** (Zynq + 16-core Epiphany).

The original Parallella images from 2015–2016 were powerful but painful to use. This project aims to bring the board into the 2020s with:

- Easy first-boot setup (hostname, root password, WiFi)
- Modern toolchain and kernel
- Clean Epiphany SDK integration
- Python support for small ML / parallel workloads
- Simple update mechanism

## Goals

- Make the Parallella actually pleasant to develop on again
- Provide a solid base for edge AI, parallel computing research, and education
- Focus on the Epiphany's strengths: low-power, regular, data-parallel workloads
- Create something maintainable that can actually be updated in 2026+

## Status

**Early stage** — repository and structure being established.

Planned features:
- Buildroot-based image with modern packages
- First-boot configuration wizard
- Easy WiFi setup
- Updated Epiphany SDK + Python bindings
- Tiny ML inference examples

## Directory Structure

```
parallella-modern/
├── README.md
├── docs/                    # Documentation
├── buildroot/
│   └── configs/             # Buildroot defconfig
├── scripts/                 # First-boot, update, wifi helpers
├── examples/
│   └── ml/                  # Tiny model examples
└── .github/workflows/       # CI for building images
```

## Contributing

This project is just getting started. Ideas, patches, and discussions are welcome — especially around:

- Epiphany programming improvements
- Small ML / parallel computing use cases
- Making the board more accessible to new users

## License

MIT License (to be confirmed)