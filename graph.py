import matplotlib.pyplot as plt
import numpy as np

# Methods used in all datasets
methods = [
    "ICON", "DialogueRNN", "COGMEN", "DialoguePCN", 
    "ResRA", "DialoguePFM", "Proposed"
]

# Emotion categories + average
emotions = ['Happy', 'Sad', 'Depressed', 'Excited', 'Exhausted', 'Frustrated', 'Afraid', 'Average']

# Data for each dataset
datasets = {
    'SEMAINE': [
        [0.725, 0.653, 0.695, 0.674, 0.603, 0.644, 0.675, 0.667],
        [0.743, 0.729, 0.704, 0.685, 0.634, 0.685, 0.685, 0.695],
        [0.757, 0.683, 0.728, 0.705, 0.626, 0.664, 0.691, 0.691],
        [0.778, 0.712, 0.749, 0.729, 0.641, 0.678, 0.684, 0.710],
        [0.801, 0.723, 0.768, 0.751, 0.665, 0.693, 0.688, 0.726],
        [0.829, 0.735, 0.796, 0.778, 0.662, 0.701, 0.693, 0.741],
        [0.835, 0.694, 0.802, 0.783, 0.655, 0.682, 0.702, 0.749],
    ],
    'AESI': [
        [0.740, 0.673, 0.705, 0.674, 0.613, 0.653, 0.643, 0.671],
        [0.754, 0.694, 0.713, 0.694, 0.646, 0.676, 0.656, 0.690],
        [0.768, 0.701, 0.736, 0.716, 0.635, 0.710, 0.653, 0.706],
        [0.785, 0.716, 0.752, 0.732, 0.649, 0.718, 0.668, 0.717],
        [0.808, 0.729, 0.777, 0.756, 0.664, 0.735, 0.675, 0.734],
        [0.834, 0.732, 0.809, 0.782, 0.674, 0.728, 0.680, 0.749],
        [0.842, 0.738, 0.818, 0.789, 0.669, 0.729, 0.671, 0.763],
    ],
    'ECF': [
        [0.743, 0.669, 0.721, 0.695, 0.626, 0.669, 0.654, 0.682],
        [0.769, 0.699, 0.724, 0.699, 0.657, 0.688, 0.667, 0.700],
        [0.775, 0.710, 0.747, 0.726, 0.647, 0.702, 0.684, 0.726],
        [0.793, 0.742, 0.765, 0.745, 0.661, 0.739, 0.688, 0.733],
        [0.819, 0.749, 0.791, 0.768, 0.673, 0.741, 0.695, 0.748],
        [0.844, 0.753, 0.818, 0.795, 0.679, 0.743, 0.697, 0.761],
        [0.856, 0.742, 0.823, 0.802, 0.685, 0.734, 0.698, 0.768],
    ],
    'MER-2024': [
        [0.722, 0.648, 0.688, 0.667, 0.609, 0.639, 0.662, 0.662],
        [0.740, 0.699, 0.708, 0.688, 0.627, 0.673, 0.670, 0.686],
        [0.755, 0.679, 0.721, 0.704, 0.633, 0.658, 0.684, 0.691],
        [0.774, 0.701, 0.744, 0.723, 0.639, 0.677, 0.682, 0.706],
        [0.796, 0.715, 0.763, 0.742, 0.658, 0.688, 0.690, 0.722],
        [0.826, 0.731, 0.791, 0.774, 0.666, 0.701, 0.695, 0.740],
        [0.832, 0.722, 0.798, 0.779, 0.659, 0.689, 0.699, 0.754],
    ],
}

# Plotting
fig, axes = plt.subplots(2, 2, figsize=(16, 10))
axes = axes.flatten()
colors = plt.cm.tab10.colors

for idx, (title, data) in enumerate(datasets.items()):
    ax = axes[idx]
    x = np.arange(len(emotions))  # position of emotion categories
    width = 0.1  # bar width
    for i, method_scores in enumerate(data):
        ax.bar(x + i * width, method_scores, width=width, label=methods[i], color=colors[i % len(colors)])
    
    ax.set_title(title)
    ax.set_xticks(x + width * 3)
    ax.set_xticklabels(emotions, rotation=45)
    ax.set_ylim(0.5, 0.9)
    

    # Add legend to each subplot with smaller font
    ax.legend(fontsize='small', loc='upper right')
    ax.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.savefig("emotion_recognition.svg", format='svg')  # Save as SVG
plt.show()
