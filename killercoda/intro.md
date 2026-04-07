> <strong>Note</strong>: logs of the *intro* background script can be found at `/var/log/killercoda`

Wait for the background script to finish.

### How to launch the desktop

The background script should have launched a VNC session already.
To be able to use a graphical session,
launch noVNC to bridge VNC (5901) to Web (6080):

`/usr/share/novnc/utils/novnc_proxy --vnc localhost:5901 --listen 6080`{{exec}}

Once the setup is complete, you can access the graphical environment here:
[Open VNC Desktop]({{TRAFFIC_HOST1_6080}}/vnc.html?autoconnect=true)

If you have trouble, you can also manually select the port here: [Access Ports]({{TRAFFIC_SELECTOR}})
