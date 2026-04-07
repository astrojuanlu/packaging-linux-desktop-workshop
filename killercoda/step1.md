
> Users can always select the Editor tab to use Theia.
> But this scenario shows how to select it by default when opening a scenario.

### Launch Desktop

Launch noVNC to bridge VNC (5901) to Web (6080):

`/usr/share/novnc/utils/novnc_proxy --vnc localhost:5901 --listen 6080`{{exec}}

Once the setup is complete, you can access the graphical environment here:
[Open VNC Desktop]({{TRAFFIC_HOST1_6080}}/vnc.html?autoconnect=true)

If you have trouble, you can also manually select the port here: [Access Ports]({{TRAFFIC_SELECTOR}})
