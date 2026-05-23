# Parallella Nemo

A modern Linux distribution and parallel exploration platform for the **Parallella 16** (Zynq + 16-core Epiphany).

## Core Idea

The Epiphany's 16 RISC cores power a **low-power parallel idea generation engine**. The system can operate in two modes:

### 1. Parallel Exploration Mode
Multiple independent explorers run simultaneously across the mesh, constantly generating ideas, alternative solutions, and novel connections without user input.

### 2. Light Chatbot / Check-in Mode
Simple proactive interactions such as casual check-ins and lightweight engagement.

Both modes use Grok (via OAuth) for high-quality responses while keeping power usage very low.

## Key Features

- True parallel exploration across 16 Epiphany cores
- Low-power always-on operation
- Proactive idea surfacing and casual check-ins
- Modern first-boot experience
- `etop` – lightweight Epiphany mesh monitor (supports E16 and E64)
- FPGA bitstream loader
- Buildroot external tree with custom packages

## Buildroot External Tree Packages

- etop
- firstboot
- explorer
- aggregator
- fpga-loader
- epiphany (kernels + python tools)

## Project Structure

```
parallella-nemo/
├── explorer/           # Parallel Idea Engine
├── external/parallella # Buildroot packages and defconfigs
├── scripts/            # First-boot installer, FPGA tools, etop
├── epiphany/           # Low-level Epiphany kernels
├── board/              # Board support
└── docs/
```

## Status

Early development. The Buildroot external tree is now buildable. Python3 + aggregator support requires further toolchain tuning.

## License

MIT License