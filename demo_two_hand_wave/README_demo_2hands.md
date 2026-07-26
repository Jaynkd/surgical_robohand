# Demo Two hands

### Expected Demo Behavior
Launching the demo opens a MuJoCo GUI window displaying dual dexterous hands performing a coordinated waving sequence.

* **Spacebar:** Pause / resume simulation
* **Double Right-Click + Drag:** Translate camera
* **Left-Click + Drag:** Rotate view around focus
* **Scroll Wheel:** Zoom in / out


### Troubleshooting
* **`GLFW initialization failed` / No display:** Ensure an active X11 display session is running (`export DISPLAY=:0`), or use X11 forwarding if connected via SSH.
