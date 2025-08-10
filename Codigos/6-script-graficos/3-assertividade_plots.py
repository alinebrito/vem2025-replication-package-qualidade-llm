import json
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import textwrap

# List all files in the directory
files = os.listdir('./data/assertividade/')

# Find all files that match the pattern
json_files = [f for f in files if f.startswith('filteredDataToResponse_') and f.endswith('.json')]

if not json_files:
    raise FileNotFoundError("No JSON files matching the pattern 'filteredDataToResponse_MODELNAME.json' found.")

# Create directories if they don't exist
os.makedirs('./plots/assertividade', exist_ok=True)

# Translation dictionary for status
status_translation = {
    'success': 'Correto',
    'error': 'Erro',
    'incorrect': 'Incorreto',
    'unknown': 'Desconhecido'
}

# Color dictionary for status
status_colors = {
    'Correto': 'green',
    'Erro': 'darkred',
    'Incorreto': 'orange',
    'Desconhecido': 'grey'
}

# Create a summary DataFrame
summary_data = {
    'Modelo': [],
    'Total de Casos de Teste': [],
    'Total de Acertos': [],
    'Total de Erros': [],
    'Total de Incorretos': [],
    'Taxa de Assertividade (%)': []
}

def format_model_name(model_name):
    if model_name == 'claude-3-haiku':
        return 'Claude 3 Haiku'
    model_name = model_name.title()
    if 'Gpt' in model_name:
        model_name = model_name.replace('Gpt', 'GPT')
    return model_name

for json_file in json_files:
    print("\n" + "="*50)
    print(f"Processing file: {json_file}")
    print("="*50)

    # Extract the model name from the file name
    model_name = json_file[len('filteredDataToResponse_'):-len('.json')]
    if model_name == 'llama-3.1-70b':
        model_name = 'llama 3.1'
    model_name = format_model_name(model_name)
    model_name = textwrap.fill(model_name, width=10)  # Wrap model name

    # Load JSON data
    with open(f'./data/assertividade/{json_file}') as f:
        data = json.load(f)

    # Process data
    total_cases = len(data)
    correct_cases = sum(1 for case in data if case.get('status') == 'success')
    error_cases = sum(1 for case in data if case.get('status') == 'error')
    incorrect_cases = sum(1 for case in data if case.get('status') == 'incorrect')
    unknown_cases = sum(1 for case in data if case.get('status') == 'unknown')

    accuracy_rate = (correct_cases / total_cases) * 100 if total_cases > 0 else 0

    summary_data['Modelo'].append(model_name)
    summary_data['Total de Casos de Teste'].append(total_cases)
    summary_data['Total de Acertos'].append(correct_cases)
    summary_data['Total de Erros'].append(error_cases)
    summary_data['Total de Incorretos'].append(incorrect_cases)
    summary_data['Taxa de Assertividade (%)'].append(accuracy_rate)

# Convert summary data to DataFrame
summary_df = pd.DataFrame(summary_data)

# Save summary data to CSV
summary_df.to_csv('./plots/assertividade/summary_data.csv', index=False)

# Plot total assertiveness
plt.figure(figsize=(10, 6))
bars = plt.barh(summary_df['Modelo'], summary_df['Taxa de Assertividade (%)'], color='gray', height=0.3)
plt.xlabel('Taxa de Assertividade (%)', fontsize=30)
plt.xticks(fontsize=24)
plt.yticks(fontsize=28)
plt.xlim(0, 100)  # Set x-axis limits from 0 to 100
plt.tight_layout()

# Add labels
for bar in bars:
    plt.text(bar.get_width(), bar.get_y() + bar.get_height()/2, f'{round(bar.get_width())}%', va='center', fontsize=28)

plt.savefig('./plots/assertividade/assertividade_total.pdf', bbox_inches='tight')
plt.close()

# Plot total error and incorrect cases
plt.figure(figsize=(10, 6))
bar_width = 0.3
index = np.arange(len(summary_df['Modelo']))

bars1 = plt.barh(index, summary_df['Total de Erros'], bar_width, label='Erros', color='black')
bars2 = plt.barh(index + bar_width, summary_df['Total de Incorretos'], bar_width, label='Incorretos', color='lightgray')

plt.xlabel('Total de Casos', fontsize=30)
plt.xticks(fontsize=24)
plt.yticks(index + bar_width / 2, summary_df['Modelo'], fontsize=30)
plt.legend(fontsize=24)
plt.xlim(0, 350)  # Set x-axis limits from 0 to 350
plt.tight_layout()

# Add labels
for bar in bars1:
    plt.text(bar.get_width(), bar.get_y() + bar.get_height()/2, f'{bar.get_width():.0f}', va='center', fontsize=28)
for bar in bars2:
    plt.text(bar.get_width(), bar.get_y() + bar.get_height()/2, f'{bar.get_width():.0f}', va='center', fontsize=28)

plt.savefig('./plots/assertividade/total_erros_incorretos.pdf', bbox_inches='tight')
plt.close()