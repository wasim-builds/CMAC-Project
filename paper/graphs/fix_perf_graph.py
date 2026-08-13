import matplotlib.pyplot as plt
import numpy as np

labels = ['Canvas Cohesion\n(Higher=Better)', 'Cost Unit\n(Lower=Better)', 'Success Rate\n(Higher=Better)']
cmac_scores = [0.88, 0.35, 0.94]
mono_scores = [0.42, 1.00, 0.41]

x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots(figsize=(8, 6))
rects1 = ax.bar(x - width/2, cmac_scores, width, label='CMAC (Ours)', color='royalblue')
rects2 = ax.bar(x + width/2, mono_scores, width, label='Monolithic Baseline', color='tomato')

ax.set_ylabel('Normalized Score / Percentage')
ax.set_title('Performance Metrics Comparison')
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=0, ha='center')
ax.legend()

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height:.2f}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.tight_layout()
plt.savefig('/run/media/wasim/2ADE-F06D/research/CMAC-Project/paper/graphs/performance_comparison.png', dpi=300)
print("Graph fixed and saved.")
