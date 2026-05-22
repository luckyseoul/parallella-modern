# Parallella Modern Roadmap

## Phase 1: Foundation (Current)
- [x] Initial repository structure
- [x] README and licensing
- [ ] Buildroot base configuration for Parallella 16
- [ ] Minimal working image (headless first)

## Phase 2: User Experience
- [ ] First-boot setup script (hostname, root password, WiFi)
- [ ] Easy WiFi configuration tool
- [ ] Basic documentation (getting started guide)

## Phase 3: Desktop & Tooling
- [ ] XFCE desktop environment (or lightweight alternative)
- [ ] Updated Epiphany SDK packaging
- [ ] Python 3 + epiphany-ml bindings with LLM kernel support

## Phase 4: RISC-Optimized LLM Workloads
- [ ] Quantized inference runtime (INT8 / INT4)
- [ ] Attention scoring and KV cache primitives
- [ ] Speculative decoding helper (tiny draft model support)
- [ ] Example RISC-optimized kernels for modern LLM components

## Phase 5: Polish & Maintenance
- [ ] Simple update mechanism
- [ ] CI for building images
- [ ] Better documentation and examples
- [ ] Community feedback loop

## Long-term Vision

Create a genuinely usable, modern Linux distribution for the Parallella that makes the Epiphany's parallel RISC capabilities relevant again for edge AI and specialized LLM workloads in 2026+. Focus on what RISC architectures do well: predictable execution, low power, and explicit parallelism for quantized and kernel-level operations.