# Parallella Modern

A modern Linux distribution and parallel exploration platform for the **Parallella 16** (Zynq + 16-core Epiphany).

## Core Idea

The Epiphany's 16 RISC cores power a **low-power parallel idea generation engine**. The system can operate in two modes:

### 1. Parallel Exploration Mode
Multiple independent explorers run simultaneously across the mesh, constantly generating ideas, alternative solutions, and novel connections without user input. This is the key differentiator versus normal single-board computers.

### 2. Light Chatbot / Check-in Mode
Simple proactive interactions such as:
- "Haven't heard from you in a while, how are things?"
- Casual follow-ups and lightweight engagement

Both modes use Grok (via OAuth) for high-quality responses while keeping power usage very low.

## Key Features

- True parallel exploration across 16 Epiphany cores
- Low-power always-on operation
- Proactive idea surfacing and casual check-ins
- Modern first-boot experience and tooling
- Supports both Epiphany III (16 cores) and Epiphany IV (64 cores) via `epiphany-mon`

## Project Structure

```
parallella-modern/
├── explorer/           # Parallel Idea Engine + Chatbot mode
│   ├── core/
│   ├── aggregator/
│   └── docs/
├── buildroot/          # Image configurations
├── scripts/            # First-boot installer, FPGA tools, epiphany-mon
├── epiphany/           # Lower-level Epiphany kernels
└── docs/
```

## Status

Early development. The Parallel Autonomous Idea Engine (with both exploration and chatbot modes) is the current focus.

## License

MIT License