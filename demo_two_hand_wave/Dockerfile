FROM python:3.10-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1-mesa-glx \
    libgl1-mesa-dri \
    libosmesa6 \
    libglfw3 \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

ENV MUJOCO_GL="osmesa"
ENV PYOPENGL_PLATFORM="osmesa"
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY package_requirements.txt .
RUN pip install --no-cache-dir -r package_requirements.txt

COPY mj_setup/ ./mj_setup/
WORKDIR /app/mj_setup

CMD ["python", "run_sim.py"]
EOF

# 6. Update docker-compose.yml
cat << 'EOF' > docker-compose.yml
version: '3.8'

services:
  headless:
    build: .
    container_name: mujoco_surgical_headless
    environment:
      - MUJOCO_GL=osmesa
    volumes:
      - ./mj_setup:/app/mj_setup
    command: python run_sim.py --steps 300

  gui:
    build: .
    container_name: mujoco_surgical_gui
    environment:
      - DISPLAY=${DISPLAY}
      - MUJOCO_GL=glfw
    volumes:
      - /tmp/.X11-unix:/tmp/.X11-unix:rw
    network_mode: host
    command: python run_sim.py --gui
