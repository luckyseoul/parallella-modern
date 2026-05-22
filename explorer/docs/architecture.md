# Parallel Autonomous Idea Engine — Architecture

## Vision

A low-power, always-on system that uses the Epiphany's 16 RISC cores to run many independent "explorers" in parallel. These explorers constantly generate ideas, alternative solutions, and novel connections without requiring user initiation.

The system also supports lighter, proactive chatbot-style interactions.

## Two Operating Modes

### 1. Parallel Exploration Mode (Primary Differentiator)
- Multiple explorers run simultaneously across the Epiphany mesh
- Each core can be assigned different roles (creative, technical, risk analysis, connections)
- Results are aggregated, evaluated by Grok, and surfaced when interesting
- This mode is difficult to replicate efficiently on normal single/quad-core boards

### 2. Light Chatbot / Check-in Mode
- Simple proactive messages such as:
  - "Haven't heard from you in a while, how are things?"
  - Casual check-ins or follow-ups
  - Lightweight conversational engagement
- Runs with very low overhead
- Uses the same Grok OAuth backend for natural responses
- Provides a gentler, more approachable entry point for users

## System Components

- **Explorer Cores** — Run on Epiphany cores (can operate in either mode)
- **Aggregator** — Collects results, deduplicates, and decides when to surface output
- **Grok Client** — Handles evaluation and natural language generation via OAuth
- **Notifier** — Delivers messages through chosen channels (console, Telegram, etc.)

## Current Status

Early development. Both modes are supported in the architecture, with the parallel exploration mode being the primary technical focus.