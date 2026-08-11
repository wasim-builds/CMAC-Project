# Collaborative Multi-Agent Canvas (CMAC)

This repository contains the prototype simulation and research paper for **"Collaborative Multi-Agent Canvas (CMAC): Hierarchical Reinforcement Learning for Long-Horizon Generative Workflows"**.

## The Research Gap
Current multimodal generative agents (like those observed in JarvisHub and VideoCoCo frameworks) fail catastrophically during long-horizon generation because monolithic architectures suffer from context decay. CMAC solves this by implementing a hierarchical Reinforcement Learning (RL) approach on a shared memory canvas.

## System Architecture
- **Director Agent:** Evaluates the overarching prompt and generates a multi-step semantic plan.
- **Worker Agents:** Specialized experts (e.g., Layout, Lighting, Render) that execute atomic updates on the Shared Canvas.
- **RL Evaluator:** Analyzes the cohesion of the canvas after every update and calculates a reward function.

## Running the Simulation

```bash
cd src
python3 simulation.py
```

## Research Paper
The LaTeX source code is formatted to IEEE Conference standards and is available in the `paper/` directory.

---
**Author:** Mohammed Wasim Khan (VIT-AP University)
