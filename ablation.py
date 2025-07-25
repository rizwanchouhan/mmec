import matplotlib.pyplot as plt
import numpy as np

# Model variants and dataset names
variants = ['Full Model (Proposed)', 'w/o ACMA', 'w/o ECIM', 'w/o REFM']
datasets = ['SEMAINE', 'AESI', 'ECF', 'MER-2024']

# F1 scores for each variant across datasets
scores = np.array([
    [0.749, 0.763, 0.768, 0.754],
    [0.724, 0.738, 0.745, 0.729],
    [0.731, 0.743, 0.752, 0.736],
    [0.734, 0.746, 0.754, 0.738]
])

# Plotting configuration
x = np.arange(len(datasets))
width = 0.2

fig, ax = plt.subplots(figsize=(10, 6))
colors = ['#FFAF00', '#F46920', '#F53255', '#F85FC1']

for i in range(len(variants)):
    ax.bar(x + i * width - width * 1.5, scores[i], width, label=variants[i], color=colors[i])

# Formatting the plot
ax.set_ylabel('Average F1 Score', fontsize=12)
ax.set_title('Ablation Study: Average F1 Scores Across Datasets', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(datasets, fontsize=11)
ax.set_ylim(0.70, 0.78)
ax.legend(fontsize=10)
ax.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.savefig("ablation.svg", format='svg')  # Save as SVG
plt.show()
