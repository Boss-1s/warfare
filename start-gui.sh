#!/bin/bash
fuser -k -n tcp 5999 2>/dev/null || true
sudo rm -f /tmp/.X99-lock
sudo rm -f /tmp/.X11-unix/X99
sudo killall Xvfb
sudo pkill -f Xvnc; sudo pkill -f websockify

# Start virtual frame buffer screen
Xvfb :99 -screen 0 1024x768x16 &
export DISPLAY=:99

# Start a lightweight window manager
fluxbox &

websockify --web=/usr/share/novnc/ 6080 localhost:5900
