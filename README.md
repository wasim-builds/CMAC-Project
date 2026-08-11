# Collaborative Multi-Agent Canvas (CMAC)

![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.10%2B-green)

This repository contains the prototype simulation and the 6-page IEEE format research paper for **"Collaborative Multi-Agent Canvas (CMAC): Hierarchical Reinforcement Learning for Long-Horizon Generative Workflows"**.

## 📖 The Research Gap
Current multimodal generative agents (like those observed in standard autoregressive LLMs) fail catastrophically during long-horizon generation because monolithic architectures suffer from context decay. CMAC solves this by implementing a hierarchical Reinforcement Learning (RL) approach on a shared memory canvas, bypassing the massive context-window bottlenecks.

## 🏗️ System Architecture
- **Director Agent:** Evaluates the overarching prompt and generates a multi-step semantic plan.
- **Worker Agents:** Specialized, lightweight experts (e.g., Layout, Lighting, Render) that execute atomic updates on the Shared Canvas.
- **RL Evaluator:** Analyzes the cohesion of the canvas after every update using Proximal Policy Optimization (PPO).

---

## 🚀 How to Clone and Test Locally

Follow these steps to run the 10,000-epoch reinforcement learning simulation on your local machine and generate the performance graphs.

### 1. Clone the Repository
```bash
git clone https://github.com/wasim-builds/CMAC-Project.git
cd CMAC-Project
```

### 2. Set Up the Environment
It is recommended to use a virtual environment to prevent dependency conflicts.
```bash
python3 -m venv env
source env/bin/activate
pip install matplotlib numpy
```

### 3. Run the Simulation
Run the core simulation script to observe the Director and Worker agents passing the canvas state.
```bash
cd src
python3 simulation.py
```
*Expected Output: The terminal will print the hierarchical routing process and report the final cohesion scores for each generative episode.*

### 4. Generate the Graphs
To mathematically verify the convergence of the CMAC architecture versus a monolithic baseline, run the plotting script:
```bash
python3 plot_results.py
```
*This will output high-resolution `convergence_graph.png` and `performance_comparison.png` files directly into the `paper/graphs/` directory.*

---

## 📄 Research Paper
The complete 6-page LaTeX source code is formatted to strict IEEE Conference standards. It contains the mathematical proofs (MDP & PPO constraints) and ablation studies.

You can find the source code in:
```
paper/main.tex
```
*(Note: To compile the paper into a PDF, we recommend uploading the `paper/` directory to Overleaf or using a local `pdflatex` distribution).*

---
**Author:** Mohammed Wasim Khan  
**Institution:** VIT-AP University  
**Contact:** wasim143mr@gmail.com  
