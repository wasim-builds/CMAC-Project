import matplotlib.pyplot as plt
import numpy as np
import os
import json

output_dir = "../paper/graphs"
os.makedirs(output_dir, exist_ok=True)

# Load results
with open("results_variance.json", "r") as f:
    results = json.load(f)

seeds = results["seeds"]
cmac = np.array(results["CMAC"])
mono = np.array(results["Monolithic"])
flat = np.array(results["Flat Multi-Agent"])

# Calculate mean and standard deviation
means = [cmac.mean(), flat.mean(), mono.mean()]
stds = [cmac.std(), flat.std(), mono.std()]
labels = ['CMAC (Ours)', 'Flat Multi-Agent', 'Monolithic']

# 1. Bar Chart with Error Bars
plt.figure(figsize=(9, 6))
x = np.arange(len(labels))
plt.bar(x, means, yerr=stds, capsize=10, color=['royalblue', 'mediumseagreen', 'tomato'], alpha=0.8)
plt.xticks(x, labels)
plt.ylabel('Average Reward (Cohesion & Length)')
plt.title('Agent Architecture Performance (Mean ± Std Dev)')
plt.grid(axis='y', alpha=0.3)

for i, v in enumerate(means):
    plt.text(i, v + 0.5, f"{v:.2f}", ha='center', fontweight='bold')

bar_path = os.path.join(output_dir, 'architecture_comparison_bar.png')
plt.savefig(bar_path, dpi=300)
print(f"✅ Generated: {bar_path}")

# 2. Fill Between Graph across Seeds
plt.figure(figsize=(9, 5))
x_seeds = np.array(seeds)

plt.plot(x_seeds, cmac, label='CMAC (Ours)', color='blue', marker='o')
plt.fill_between(x_seeds, cmac - cmac.std(), cmac + cmac.std(), color='blue', alpha=0.2)

plt.plot(x_seeds, flat, label='Flat Multi-Agent', color='green', marker='s')
plt.fill_between(x_seeds, flat - flat.std(), flat + flat.std(), color='green', alpha=0.2)

plt.plot(x_seeds, mono, label='Monolithic Baseline', color='red', marker='^')
plt.fill_between(x_seeds, mono - mono.std(), mono + mono.std(), color='red', alpha=0.2)

plt.title('Performance Variance Across Seeds')
plt.xlabel('Seed')
plt.ylabel('Reward')
plt.xticks(seeds)
plt.legend()
plt.grid(True, alpha=0.3)

variance_path = os.path.join(output_dir, 'seed_variance_fill.png')
plt.savefig(variance_path, dpi=300)
print(f"✅ Generated: {variance_path}")
print("Graphs successfully generated for the CMAC paper!")
