import json
import os
import glob
import pandas as pd
import numpy as np
from scipy.stats import kruskal

# Initialize dictionaries to hold the maintainability issues and technical debt per model
maintainability_issues_dict = {}
technical_debt_dict = {}

# Iterate over all JSON files in the directory
json_files = glob.glob('./data/sonar-metrics/all_metrics_*.json')

for json_file in json_files:
    # Extract model_name from the filename
    model_name = os.path.basename(json_file).split('_')[2].split('.')[0]
    
    # Create directory for the model if it doesn't exist
    model_dir = f'./plots/sonar-metrics/{model_name}'
    os.makedirs(model_dir, exist_ok=True)
    
    # Load JSON data
    with open(json_file) as f:
        data = json.load(f)
    
    # Extract maintainability issues and technical debt
    maintainability_issues = [item['maintainability']['issues'] if 'maintainability' in item and 'issues' in item['maintainability'] else '0' for item in data]
    technical_debt = [item['maintainability']['technical_debt'] if 'maintainability' in item and 'technical_debt' in item['maintainability'] else '0' for item in data]
    
    # Convert to numeric
    maintainability_issues = pd.to_numeric(maintainability_issues, errors='coerce')
    technical_debt = pd.to_numeric(technical_debt, errors='coerce')
    
    # Store the maintainability issues and technical debt in the dictionaries
    maintainability_issues_dict[model_name] = maintainability_issues
    technical_debt_dict[model_name] = technical_debt

# Calculate statistics for each model
maintainability_paragraph = ""
technical_debt_paragraph = ""

maintainability_stats = []
technical_debt_stats = []

for model_name, issues in maintainability_issues_dict.items():
    if len(issues) > 0:
        min_issues = issues.min()
        max_issues = issues.max()
        median_issues = np.median(issues)
    else:
        min_issues = max_issues = median_issues = 'N/A'
    
    maintainability_paragraph += f"Para o modelo {model_name}, os valores de maintainability issues variam entre {min_issues} e {max_issues}, com mediana de {median_issues}. \n"
    maintainability_stats.append([model_name, min_issues, max_issues, median_issues])

for model_name, debt in technical_debt_dict.items():
    if len(debt) > 0:
        min_debt = debt.min()
        max_debt = debt.max()
        median_debt = np.median(debt)
    else:
        min_debt = max_debt = median_debt = 'N/A'
    
    technical_debt_paragraph += f"Para o modelo {model_name}, os valores de technical debt variam entre {min_debt} e {max_debt}, com mediana de {median_debt}. \n"
    technical_debt_stats.append([model_name, min_debt, max_debt, median_debt])

print("Maintainability Issues:\n")
print(maintainability_paragraph)
print("\nTechnical Debt:\n")
print(technical_debt_paragraph)

# Save statistics to CSV files
for model_name in maintainability_issues_dict.keys():
    model_dir = f'./plots/sonar-metrics/{model_name}'
    maintainability_df = pd.DataFrame([stat for stat in maintainability_stats if stat[0] == model_name], columns=['Model', 'Min Issues', 'Max Issues', 'Median Issues'])
    technical_debt_df = pd.DataFrame([stat for stat in technical_debt_stats if stat[0] == model_name], columns=['Model', 'Min Debt', 'Max Debt', 'Median Debt'])
    
    maintainability_df.to_csv(f'{model_dir}/maintainability_issues_stats.csv', index=False)
    technical_debt_df.to_csv(f'{model_dir}/technical_debt_stats.csv', index=False)

# Perform Kruskal-Wallis test for all models and save results
kruskal_results = []

model_names = list(maintainability_issues_dict.keys())

# Perform Kruskal-Wallis test for maintainability issues
maintainability_data = [maintainability_issues_dict[model] for model in model_names if len(maintainability_issues_dict[model]) > 0]
if len(maintainability_data) > 1:
    stat, p_value = kruskal(*maintainability_data)
    print(f"Teste de Kruskal-Wallis para maintainability issues: p-value={p_value}")
    kruskal_results.append(['All Models', 'maintainability issues', stat, p_value])
else:
    print("Dados insuficientes para realizar o teste de Kruskal-Wallis para maintainability issues.")

# Perform Kruskal-Wallis test for technical debt
technical_debt_data = [technical_debt_dict[model] for model in model_names if len(technical_debt_dict[model]) > 0]
if len(technical_debt_data) > 1:
    stat, p_value = kruskal(*technical_debt_data)
    print(f"Teste de Kruskal-Wallis para technical debt: p-value={p_value}")
    kruskal_results.append(['All Models', 'technical debt', stat, p_value])
else:
    print("Dados insuficientes para realizar o teste de Kruskal-Wallis para technical debt.")

# Save Kruskal-Wallis test results to CSV file
kruskal_df = pd.DataFrame(kruskal_results, columns=['Model 1', 'Metric', 'H Statistic', 'P Value'])
kruskal_df.to_csv('./plots/sonar-metrics/kruskal_test_results.csv', index=False)