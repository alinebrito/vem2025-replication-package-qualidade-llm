import json
import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

with open('./data/caracterizacao/dataUpdated.json') as f:
    data = json.load(f)

submissions = [item['stat']['total_submitted'] for item in data]
acceptances = [item['stat']['total_acs'] for item in data]
discussions = [item['discussionData']['commentCount'] for item in data]
likes = [item['additionalData']['likes'] for item in data]
dislikes = [item['additionalData']['dislikes'] for item in data]

# Create DataFrame to calculate statistics
df = pd.DataFrame({
    'Submissões': submissions,
    'Aceitações': acceptances,
    'Discussões': discussions,
    'Likes': likes,
    'Dislikes': dislikes
})

# Calculate statistics
stats = df.describe()
stats.loc['median'] = df.median()
print(stats)

# Reorganize data to place discussions last
data_to_plot = [submissions, acceptances, likes, dislikes, discussions]
colors = ['lightblue', 'lightgreen', 'lightcoral', 'lightgoldenrodyellow', 'red']
labels = ['(a) Submissões', '(b) Aceitações', '(c) Likes', '(d) Dislikes', '(e) Discussões']
y_labels = [
    'Número de submissões (log)',
    'Número de submissões aceitas (log)',
    'Número de likes (log)',
    'Número de dislikes (log)',
    'Número de discussões (log)'
]

# Verifique se o diretório 'plots' existe, caso contrário, crie-o
if not os.path.exists('plots'):
    os.mkdir('plots')

for i, (data, color, label, y_label) in enumerate(zip(data_to_plot, colors, labels, y_labels)):
    fig, ax = plt.subplots(figsize=(12, 24))  # Aumente bastante a altura da figura
    
    box = ax.boxplot(data, patch_artist=True, widths=0.6)  # Increase the width of the boxes
    for patch in box['boxes']:
        patch.set_facecolor(color)
    ax.set_yscale('log')
    
    # Add labels to the median and change the median line color to white
    for median in box['medians']:
        median_value = median.get_ydata()[0]
        median.set_color('black')
        if median_value >= 1_000_000:
            formatted_value = f'{median_value/1_000_000:.2f}M'
        elif median_value >= 10_000:
            formatted_value = f'{median_value/1_000:.2f}k'
        else:
            formatted_value = f'{median_value:.2f}'
        ax.text(median.get_xdata()[0] + 0.3, median_value * 1.2, formatted_value, 
                verticalalignment='center', horizontalalignment='center', fontsize=80, color='black', fontweight='bold')  # Aumente bastante o tamanho da fonte
    
    # Adjust y-axis limits to include the lowest and highest values
    y_min = min(data)
    y_max = max(data)
    
    # Set y-axis labels to include 4 main values
    yticks = np.logspace(np.log10(y_min), np.log10(y_max), num=5)
    ax.set_yticks(yticks)
    ax.set_yticklabels([f'$10^{int(np.log10(tick))}$' for tick in yticks], fontsize=80)
    
    # Remover labels do eixo X
    ax.set_xlabel('')
    
    # Add label to the Y-axis
    ax.set_ylabel(y_label, fontsize=80)  # Aumente bastante o tamanho da fonte
    
    # Remove numerical values from the base of the boxplot
    ax.set_xticks([])
    
    # Add grid lines on the Y-axis only at the main values
    ax.grid(True, which='major', axis='y', linestyle='-', linewidth=0.5)
    
    # Adjust layout to avoid overlap
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    
    # Save each plot with high resolution as PDF
    plt.savefig(f'plots/caracterizacao/boxplot_{i}.pdf', dpi=300, bbox_inches='tight')
    
    # Close the figure to avoid memory issues
    plt.close(fig)