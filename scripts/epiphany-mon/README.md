# epiphany-mon

Lightweight monitor for Epiphany mesh utilization.

Supports both Epiphany III (16 cores) and Epiphany IV (64 cores).

## Build

```bash
make
```

## Usage

```bash
./epiphany-mon          # Default: 16 cores
./epiphany-mon 64       # 64-core mode (E64)
```

Press `q` to quit.

## Notes

- Currently uses simulated data
- Real version will read from shared memory regions used by the Parallel Idea Engine
- Designed to be very lightweight

## Future

- Real shared memory integration
- ARM load + memory stats
- Color support
- Configurable update rate