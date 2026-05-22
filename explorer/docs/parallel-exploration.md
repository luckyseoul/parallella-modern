# Parallel Exploration as the Core Differentiator

The Epiphany's 16-core mesh allows us to run many independent explorers simultaneously. This is the central value proposition.

## Why This Matters

- A Raspberry Pi (or most normal SBCs) would have to time-slice these explorers
- The Epiphany can run all 16 in true parallel with very low power
- This enables "always-on idea generation" at a scale that's impractical on conventional hardware

## Explorer Specialization (Future)

Different cores can be given different roles:

- Core 0-3: Creative / divergent thinking
- Core 4-7: Technical feasibility
- Core 8-11: Constraint checking
- Core 12-15: Novel connections / synthesis

## Communication Strategy

- Cores mostly work independently
- Periodic result dumping into shared memory
- ARM-side aggregator pulls and processes results

This design keeps the Epiphany's parallelism at the center of the system.