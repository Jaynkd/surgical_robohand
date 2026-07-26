# Surgical_Robotics_hands
Robotics hand simulation for surgical robotics

Standalone dexterous robotic hand simulation in MuJoCo for surgical robotics research. Built to evaluate fine contact dynamics, tendon actuation, and micro-grasping of surgical instruments (e.g., suture needles).

---

## Prerequisites

### Ubuntu / Debian Host Setup
If running directly on Linux without Docker, ensure Python 3, `pip`, and `venv` are installed on your host system:

```bash
sudo apt update
sudo apt install -y python3-pip python3-venv

![Dual Hands Wave Demo](demo_two_hand_wave/media/your_image_name.png)

## Running the Demo
```bash
python demo_two_hand_wave/run_mjsim.py
