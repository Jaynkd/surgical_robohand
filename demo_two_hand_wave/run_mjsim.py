import argparse
import time
import numpy as np
import mujoco
import mujoco.viewer
from demo_model import load_dual_hands_model

def apply_dual_shadow_controls(data, t):
    """Drive all actuators across both left and right Shadow hands."""
    num_actuators = len(data.ctrl)
    if num_actuators > 0:
        half = num_actuators // 2

        # Left Hand control wave
        for i in range(half):
            data.ctrl[i] = 0.3 + 0.35 * np.sin(1.8 * t + i * 0.15)

        # Right Hand control wave (slightly phase-shifted)
        for i in range(half, num_actuators):
            data.ctrl[i] = 0.3 + 0.35 * np.sin(1.8 * t + (i - half) * 0.15 + 0.5)

def run_headless(steps=300, output_file="dual_hands_demo.mp4"):
    print("[Headless] Loading dual Shadow Hand scene...")
    model = load_dual_hands_model()
    data = mujoco.MjData(model)
    renderer = mujoco.Renderer(model, height=720, width=1280)

    import imageio
    frames = []

    for step in range(steps):
        t = step * model.opt.timestep
        apply_dual_shadow_controls(data, t)
        mujoco.mj_step(model, data)
        renderer.update_scene(data)
        frames.append(renderer.render())

    out_path = f"./{output_file}"
    imageio.mimsave(out_path, frames, fps=30)
    print(f"[Headless] Done! Saved video to {out_path}")

def run_interactive():
    print("[Interactive] Launching Dual Shadow Hands Viewer...")
    model = load_dual_hands_model()
    data = mujoco.MjData(model)

    viewer = mujoco.viewer.launch_passive(model, data)
    print("[Interactive] Viewer active! Press Esc or close window to exit.")

    start_time = time.time()
    try:
        while viewer.is_running():
            step_start = time.time()
            t = time.time() - start_time

            apply_dual_shadow_controls(data, t)
            mujoco.mj_step(model, data)
            viewer.sync()

            time_until_next_step = model.opt.timestep - (time.time() - step_start)
            if time_until_next_step > 0:
                time.sleep(time_until_next_step)
    finally:
        viewer.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--gui", action="store_true")
    parser.add_argument("--steps", type=int, default=300)
    args = parser.parse_args()

    if args.gui:
        run_interactive()
    else:
        run_headless(steps=args.steps)
