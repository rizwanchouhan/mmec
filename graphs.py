import pandas as pd
import matplotlib.pyplot as plt

# Define the data from the LaTeX table
data = {
    "Method": ["ICON", "DialogueRNN", "COGMEN", "MECHM (Our)"],
    "Happy_SEMAINE": [0.725, 0.743, 0.757, 0.855],
    "Sad_SEMAINE": [0.653, 0.735, 0.683, 0.694],
    "Depressed_SEMAINE": [0.695, 0.704, 0.728, 0.834],
    "Excited_SEMAINE": [0.674, 0.685, 0.705, 0.804],
    "Exhausted_SEMAINE": [0.603, 0.634, 0.626, 0.665],
    "Frustrated_SEMAINE": [0.644, 0.685, 0.664, 0.654],
    "Afraid_SEMAINE": [0.675, 0.685, 0.691, 0.699],
    "Happy_AESI": [0.740, 0.754, 0.768, 0.865],
    "Sad_AESI": [0.673, 0.694, 0.701, 0.745],
    "Depressed_AESI": [0.705, 0.713, 0.736, 0.846],
    "Excited_AESI": [0.674, 0.694, 0.716, 0.814],
    "Exhausted_AESI": [0.613, 0.646, 0.635, 0.674],
    "Frustrated_AESI": [0.653, 0.676, 0.735, 0.729],
    "Afraid_AESI": [0.643, 0.656, 0.653, 0.671],
    "Happy_ECF": [0.743, 0.769, 0.775, 0.876],
    "Sad_ECF": [0.669, 0.699, 0.758, 0.713],
    "Depressed_ECF": [0.721, 0.724, 0.747, 0.853],
    "Excited_ECF": [0.695, 0.699, 0.726, 0.823],
    "Exhausted_ECF": [0.626, 0.657, 0.647, 0.685],
    "Frustrated_ECF": [0.669, 0.688, 0.747, 0.734],
    "Afraid_ECF": [0.654, 0.667, 0.684, 0.698]
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(data)

# Plot each method separately
methods = ["ICON", "DialogueRNN", "COGMEN", "MECHM (Our)"]
emotions = ["Happy", "Sad", "Depressed", "Excited", "Exhausted", "Frustrated", "Afraid"]
datasets = ["SEMAINE", "AESI", "ECF"]

for dataset in datasets:
    fig, axs = plt.subplots(figsize=(10, 6))
    df_plot = df[["Method", f"Happy_{dataset}", f"Sad_{dataset}", f"Depressed_{dataset}", f"Excited_{dataset}", f"Exhausted_{dataset}", f"Frustrated_{dataset}", f"Afraid_{dataset}"]].set_index("Method")
    df_plot.columns = emotions
    df_plot.T.plot(kind="bar", ax=axs, color=['#f9bc02', '#0392ce', '#8601b0', '#fd5308'], width=0.8)
    axs.set_title(f"Performance Comparison using {dataset} Dataset")
    axs.set_ylabel("Values")
    axs.set_xlabel("Emotions")
    axs.grid(False)
    plt.xticks(rotation=0)
    plt.legend(title="Methods", labels=methods)
    # Annotate each bar with its specific value
    for p in axs.patches:
        axs.annotate(str(round(p.get_height(), 1)), (p.get_x() + p.get_width() / 1., p.get_height()), ha='center', va='center', xytext=(-8, 4), textcoords='offset points')

    plt.tight_layout()
    plt.savefig(f"{dataset}_comparison.svg", format="svg")  # Save as SVG
    plt.show()