# Parallel Autonomous Idea Engine — Architecture

## Vision

A low-power, always-on system that uses the Epiphany's 16 RISC cores to run many independent "explorers" in parallel. These explorers constantly generate ideas, alternative solutions, and novel connections without requiring user initiation.

The key differentiator is **true parallel exploration** at very low power — something difficult to replicate efficiently on normal single/quad-core boards.

## High-Level Flow

1. **Epiphany Cores** — Each core runs a lightweight, independent explorer
2. **Aggregation** — Results are collected and deduplicated on the ARM side
3. **Evaluation** — Interesting outputs are sent to Grok (via OAuth) for refinement
4. **Notification** — High-value ideas are pushed to the user

## Core Explorer Design

Each Epiphany core will run a small, independent loop that:

- Maintains its own context / prompt variation
- Generates ideas using a lightweight local model or templates
- Periodically reports promising outputs to the aggregator
- Can be specialized (one core does creative thinking, another does technical feasibility, etc.)

## Communication Model

- Explicit shared memory regions between Epiphany cores and ARM
- Simple message passing for results
- Low overhead — cores mostly work independently

## Next Steps

- Define the core explorer runtime
- Build basic aggregation layer
- Integrate Grok OAuth for evaluation
- Design notification system

This architecture prioritizes the Epiphany's parallelism as the central value.