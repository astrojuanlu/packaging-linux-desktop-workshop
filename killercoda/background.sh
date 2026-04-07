#!/bin/bash

set -x  # to test stderr output in /var/log/killercoda

echo Installing...  # to test stdout output in /var/log/killercoda

# 1. Update and install lightweight Desktop + VNC + noVNC
sudo apt-get update
sudo apt-get install --no-install-recommends -y \
    xfce4 xfce4-goodies tightvncserver novnc python3-websockify \
    git build-essential pkg-config python3-dev libgirepository-2.0-dev libcairo2-dev gir1.2-gtk-3.0 libcanberra-gtk3-module \
    dbus-x11 \
    snapd \
    && rm -rf /var/lib/apt/lists/*

sudo snap install astral-uv --classic

# 2. Start VNC server (Password is 'password' for simplicity)
mkdir -p ~/.vnc
echo "password" | vncpasswd -f > ~/.vnc/passwd
chmod 600 ~/.vnc/passwd

# 3. Start the VNC session on display :1
vncserver :1 -geometry 1280x800 -depth 24

# 4. Launch noVNC to bridge VNC (5901) to Web (6080)
# This runs in the background
# TODO: Think about what to do with this
# /usr/share/novnc/utils/novnc_proxy --vnc localhost:5901 --listen 6080 &

touch /tmp/finished