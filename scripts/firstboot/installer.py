#!/usr/bin/env python3
"""
Parallella Modern - First Boot Installer
Modeled after the modern Ubuntu Server installer experience.
"""

import os
import sys
import subprocess
import time
from dialog import Dialog

# Constants
SETUP_FLAG = "/etc/parallella-setup-done"
DIALOG_TITLE = "Parallella Modern Setup"

def run_cmd(cmd):
    """Run a shell command and return (success, output)"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.returncode == 0, result.stdout.strip()
    except Exception:
        return False, ""

def check_wifi():
    """Check if WiFi interface exists"""
    success, output = run_cmd("iw dev | grep Interface")
    return success and "Interface" in output

def setup_wifi(d):
    """WiFi configuration flow"""
    d.infobox("Scanning for WiFi networks...", width=40, height=5)
    time.sleep(1.5)

    success, networks = run_cmd("iwlist scan 2>/dev/null | grep ESSID | cut -d: -f2 | tr -d '\"' | head -10")
    if not success or not networks:
        d.msgbox("No WiFi networks found or WiFi not available.\n\nYou can configure it later with 'parallella-wifi'.", title=DIALOG_TITLE)
        return

    choices = [(net, "") for net in networks.split('\n') if net.strip()]
    if not choices:
        choices = [("No networks found", "")]

    code, tag = d.menu("Select WiFi Network",
                       choices=choices,
                       title="WiFi Setup",
                       width=60, height=15)

    if code != d.OK or tag == "No networks found":
        return

    ssid = tag
    code, password = d.passwordbox(f"Enter password for {ssid}:",
                                   title="WiFi Password",
                                   width=50)

    if code != d.OK:
        return

    # Create wpa_supplicant config
    config = f"""
network={{
    ssid="{ssid}"
    psk="{password}"
}}
"""
    with open("/etc/wpa_supplicant/wpa_supplicant.conf", "w") as f:
        f.write(config)

    d.infobox("Connecting to WiFi...", width=40, height=5)
    run_cmd("systemctl restart wpa_supplicant")
    time.sleep(3)

    success, _ = run_cmd("ping -c 1 8.8.8.8")
    if success:
        d.msgbox(f"Successfully connected to {ssid}!", title="WiFi")
    else:
        d.msgbox("Connection may have failed. You can retry later.", title="WiFi")

def main():
    if os.path.exists(SETUP_FLAG):
        sys.exit(0)

    d = Dialog(dialog="dialog", autowidgetsize=True)
    d.set_background_title("Parallella Modern Installer")

    # Welcome
    d.msgbox(
        "Welcome to Parallella Modern\n\n"
        "This setup will guide you through basic configuration.\n\n"
        "Press OK to continue.",
        title=DIALOG_TITLE,
        width=60, height=12
    )

    # Network / WiFi
    if check_wifi():
        code, tag = d.yesno("Would you like to configure WiFi now?",
                            title="Network Setup",
                            width=50, height=8)
        if code == d.OK:
            setup_wifi(d)
    else:
        d.msgbox("No WiFi hardware detected. Skipping WiFi setup.",
                 title="Network")

    # Root password
    code, password = d.passwordbox("Set root password:", title="Root Password", width=50)
    if code == d.OK and password:
        run_cmd(f'echo "root:{password}" | chpasswd')

    # SSH
    code, tag = d.yesno("Enable SSH server?", title="SSH", defaultno=False)
    if code == d.OK:
        run_cmd("systemctl enable sshd || systemctl enable ssh")
        run_cmd("systemctl start sshd || systemctl start ssh")

    # Updates
    code, tag = d.yesno("Check for system updates now?", title="Updates")
    if code == d.OK:
        d.infobox("Checking for updates...", width=40, height=5)
        run_cmd("apt-get update && apt-get upgrade -y || true")

    # Finish
    d.msgbox(
        "Setup complete!\n\n"
        "The system will now finish configuration and reboot.\n\n"
        "You can re-run this setup later if needed.",
        title="Complete",
        width=55, height=12
    )

    # Mark as done
    with open(SETUP_FLAG, "w") as f:
        f.write("1\n")

    # Reboot
    time.sleep(2)
    os.system("reboot")

if __name__ == "__main__":
    main()