#!/bin/bash

set -x  # to test stderr output in /var/log/killercoda

echo Installing...  # to test stdout output in /var/log/killercoda

export DEBIAN_FRONTEND=noninteractive

# 0. Some configurations
echo '# Override PS1 with red prompt' >> /root/.bashrc
echo 'export PS1="\[\033[01;31m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]# "' >> /root/.bashrc

# 1. Update and install lightweight Desktop + VNC + noVNC, plus other packages
sudo -E apt-get update
sudo -E apt-get install --no-install-recommends -y \
    xfce4 xfce4-goodies tightvncserver novnc python3-websockify \
    git build-essential pkg-config python3-dev libgirepository-2.0-dev libcairo2-dev gir1.2-gtk-3.0 libcanberra-gtk3-module \
    dbus-x11 xfonts-base x11-xserver-utils \
    snapd \
    python3.12-venv \
    && rm -rf /var/lib/apt/lists/*

sudo snap install astral-uv --classic

# 2. Start VNC server (Password is 'password' for simplicity)
mkdir -p /home/ubuntu/.vnc
echo "password" | vncpasswd -f > /home/ubuntu/.vnc/passwd
chown -R ubuntu:ubuntu /home/ubuntu/.vnc
chmod 600 /home/ubuntu/.vnc/passwd

# 3. Start the VNC session on display :1
sudo -i -u ubuntu vncserver :1 -geometry 1280x800 -depth 24

touch /tmp/finished