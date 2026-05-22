# First-Boot Installer Design

## Philosophy
Modeled after the modern Ubuntu Server installer experience — clean, guided, professional text UI.

## Technology
- Python 3 + `python3-dialog`
- Runs as a systemd oneshot service on first boot only
- Uses `/dev/tty1` for clean full-screen experience

## Flow
1. Welcome screen
2. WiFi / Network configuration
3. Root password setup
4. SSH enablement
5. Optional system update
6. Completion + reboot

## Files
- `installer.py` — Main installer logic
- `parallella-firstboot.service` — systemd unit that triggers it

## Future Improvements
- Better WiFi scanning
- User creation instead of just root
- Progress bars during long operations
- Support for Ethernet + advanced networking