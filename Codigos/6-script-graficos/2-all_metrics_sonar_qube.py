import json
import os
import glob
import matplotlib.pyplot as plt
import pandas as pd
import textwrap

# Ensure the 'plots/sonar-metrics' directory exists
if not os.path.exists('plots/sonar-metrics'):
    os.makedirs('plots/sonar-metrics')

# Initialize dictionaries to hold the sum of various metrics per LLM
maintainability_issues_total = {}
technical_debt_total = {}
# reliability_issues_total = {}
# security_issues_total = {}
# avg_lines_of_code = {}
# technical_debt_ratio_total = {}
# avg_cognitive_complexity = {}
# avg_cyclomatic_complexity = {}

def format_model_name(model_name):
    if model_name == 'claude-3-haiku':
        return 'Claude 3 Haiku'
    model_name = model_name.title()
    if 'Gpt' in model_name:
        model_name = model_name.replace('Gpt', 'GPT')
    return model_name

# Iterate over all JSON files in the directory
json_files = glob.glob('./data/sonar-metrics/all_metrics_*.json')

for json_file in json_files:
    # Extract model_name from the filename
    model_name = os.path.basename(json_file).split('_')[2].split('.')[0]
    
    # Ensure the model-specific directory exists
    model_plot_dir = f'plots/sonar-metrics/{model_name}'
    if not os.path.exists(model_plot_dir):
        os.makedirs(model_plot_dir)
    
    # Load JSON data
    with open(json_file) as f:
        data = json.load(f)
    
    # Extract relevant metrics
    maintainability_issues = [
        int(item['maintainability'].get('issues', 0)) for item in data
    ]
    technical_debt = [
        int(item['maintainability'].get('technical_debt', 0)) for item in data
    ]
    # reliability_issues = [
    #     int(item['reliability'].get('issues', 0)) for item in data
    # ]
    # security_issues = [
    #     int(item['security'].get('issues', 0)) for item in data
    # ]
    # lines_of_code = [
    #     int(item['size'].get('lines_of_code', 0)) for item in data
    # ]
    # technical_debt_ratio = [
    #     float(item['maintainability'].get('technical_debt_ratio', 0)) for item in data
    # ]
    # cognitive_complexity = [
    #     int(item['complexity'].get('cognitive_complexity', 0)) for item in data
    # ]
    # cyclomatic_complexity = [
    #     int(item['complexity'].get('cyclomatic_complexity', 0)) for item in data
    # ]
    
    # Sum up the total issues and calculate averages for this LLM
    total_issues = sum(maintainability_issues)
    total_technical_debt = sum(technical_debt)
    # total_reliability_issues = sum(reliability_issues)
    # total_security_issues = sum(security_issues)
    # avg_loc = sum(lines_of_code) / len(lines_of_code) if lines_of_code else 0
    # total_technical_debt_ratio = sum(technical_debt_ratio) / len(technical_debt_ratio) if technical_debt_ratio else 0
    # avg_cognitive_complexity_value = sum(cognitive_complexity) / len(cognitive_complexity) if cognitive_complexity else 0
    # avg_cyclomatic_complexity_value = sum(cyclomatic_complexity) / len(cyclomatic_complexity) if cyclomatic_complexity else 0
    
    # Store in the dictionaries
    if model_name == 'llama-3':
        model_name = 'llama 3.1'
    model_name = format_model_name(model_name)
    maintainability_issues_total[model_name] = total_issues
    technical_debt_total[model_name] = total_technical_debt
    # reliability_issues_total[model_name] = total_reliability_issues
    # security_issues_total[model_name] = total_security_issues
    # avg_lines_of_code[model_name] = avg_loc
    # technical_debt_ratio_total[model_name] = total_technical_debt_ratio
    # avg_cognitive_complexity[model_name] = avg_cognitive_complexity_value
    # avg_cyclomatic_complexity[model_name] = avg_cyclomatic_complexity_value
    
    # Create a DataFrame and save to CSV
    df = pd.DataFrame({
        'maintainability_issues': maintainability_issues,
        'technical_debt': technical_debt,
        # 'reliability_issues': reliability_issues,
        # 'security_issues': security_issues,
        # 'lines_of_code': lines_of_code,
        # 'technical_debt_ratio': technical_debt_ratio,
        # 'cognitive_complexity': cognitive_complexity,
        # 'cyclomatic_complexity': cyclomatic_complexity
    })
    df.to_csv(f'{model_plot_dir}/{model_name}_additional_metrics_data.csv', index=False)

# Sort the models to have consistent ordering
models = sorted(maintainability_issues_total.keys())

# Invert the order of 'gpt-4' and 'gemini'
if 'GPT-4' in models and 'Gemini' in models:
    gpt4_index = models.index('GPT-4')
    gemini_index = models.index('Gemini')
    models[gpt4_index], models[gemini_index] = models[gemini_index], models[gpt4_index]

# Wrap model names to fit in the plot
wrapped_models = [textwrap.fill(model, width=10) for model in models]

# Get values in the same order
issues = [maintainability_issues_total[model] for model in models]
technical_debt_values = [technical_debt_total[model] for model in models]
# reliability_issues_values = [reliability_issues_total[model] for model in models]
# security_issues_values = [security_issues_total[model] for model in models]
# avg_loc_values = [avg_lines_of_code[model] for model in models]
# technical_debt_ratio_values = [technical_debt_ratio_total[model] for model in models]
# avg_cognitive_complexity_values = [avg_cognitive_complexity[model] for model in models]
# avg_cyclomatic_complexity_values = [avg_cyclomatic_complexity[model] for model in models]

# Plot for maintainability issues
plt.figure(figsize=(10, 6))
bars = plt.barh(wrapped_models, issues, color='gray', height=0.3)
plt.xlabel('Total Issues de Manutenibilidade', fontsize=30)
plt.xticks(fontsize=24)
plt.yticks(fontsize=28)
plt.xlim(0, 1000)  # Set x-axis limit to 1000
plt.tight_layout()

# Add labels
for bar in bars:
    plt.text(bar.get_width(), bar.get_y() + bar.get_height()/2, f'{bar.get_width():.0f}', va='center', fontsize=24)

plt.savefig('plots/sonar-metrics/maintainability_issues_per_llm.pdf')
plt.close()

# Plot for technical debt
plt.figure(figsize=(10, 6))
bars = plt.barh(wrapped_models, technical_debt_values, color='darkgray', height=0.3)
plt.xlabel('Total Dívida Técnica', fontsize=30)
plt.xticks([500, 1500, 2500, 3500, 4500], fontsize=24)  # Set specific xticks
plt.yticks(fontsize=28)
plt.xlim(0, 4500)  # Set x-axis limit to 4500
plt.tight_layout()

# Add labels
for bar in bars:
    plt.text(bar.get_width(), bar.get_y() + bar.get_height()/2, f'{bar.get_width():.0f}', va='center', fontsize=24)

plt.savefig('plots/sonar-metrics/technical_debt_per_llm.pdf')
plt.close()

# Plot for reliability issues
# plt.figure(figsize=(10, 6))
# bars = plt.barh(wrapped_models, reliability_issues_values, color='blue')
# plt.xlabel('Quantidade Total de Problemas de Confiabilidade')
# plt.ylabel('Modelo LLM')
# plt.tight_layout()
# plt.xticks(fontsize=24)
# plt.yticks(fontsize=24)

# Add labels
# for bar in bars:
#     plt.text(bar.get_width() - 5, bar.get_y() + bar.get_height()/2, f'{bar.get_width():.0f}', va='center', fontsize=24)

# plt.savefig('plots/sonar-metrics/reliability_issues_per_llm.pdf')
# plt.close()

# Plot for security issues
# plt.figure(figsize=(10, 6))
# bars = plt.barh(wrapped_models, security_issues_values, color='red')
# plt.xlabel('Quantidade Total de Problemas de Segurança')
# plt.ylabel('Modelo LLM')
# plt.tight_layout()
# plt.xticks(fontsize=24)
# plt.yticks(fontsize=24)

# Add labels
# for bar in bars:
#     plt.text(bar.get_width() - 5, bar.get_y() + bar.get_height()/2, f'{bar.get_width():.0f}', va='center', fontsize=24)

# plt.savefig('plots/sonar-metrics/security_issues_per_llm.pdf')
# plt.close()

# Plot for average lines of code
# plt.figure(figsize=(10, 6))
# bars = plt.barh(wrapped_models, avg_loc_values, color='green')
# plt.xlabel('Quantidade Média de Linhas de Código')
# plt.ylabel('Modelo LLM')
# plt.tight_layout()
# plt.xticks(fontsize=24)
# plt.yticks(fontsize=24)

# Add labels
# for bar in bars:
#     plt.text(bar.get_width() - 5, bar.get_y() + bar.get_height()/2, f'{bar.get_width():.0f}', va='center', fontsize=24)

# plt.savefig('plots/sonar-metrics/avg_lines_of_code_per_llm.pdf')
# plt.close()

# Plot for technical debt ratio
# plt.figure(figsize=(10, 6))
# bars = plt.barh(wrapped_models, technical_debt_ratio_values, color='purple')
# plt.xlabel('Razão de Dívida Técnica')
# plt.ylabel('Modelo LLM')
# plt.tight_layout()
# plt.xticks(fontsize=24)
# plt.yticks(fontsize=24)

# Add labels
# for bar in bars:
#     plt.text(bar.get_width() - 5, bar.get_y() + bar.get_height()/2, f'{bar.get_width():.2f}', va='center', fontsize=24)

# plt.savefig('plots/sonar-metrics/technical_debt_ratio_per_llm.pdf')
# plt.close()

# Plot for average cognitive complexity
# plt.figure(figsize=(10, 6))
# bars = plt.barh(wrapped_models, avg_cognitive_complexity_values, color='orange')
# plt.xlabel('Complexidade Cognitiva Média')
# plt.ylabel('Modelo LLM')
# plt.tight_layout()
# plt.xticks(fontsize=24)
# plt.yticks(fontsize=24)

# Add labels
# for bar in bars:
#     plt.text(bar.get_width() - 5, bar.get_y() + bar.get_height()/2, f'{bar.get_width():.2f}', va='center', fontsize=24)

# plt.savefig('plots/sonar-metrics/avg_cognitive_complexity_per_llm.pdf')
# plt.close()

# Plot for average cyclomatic complexity
# plt.figure(figsize=(10, 6))
# bars = plt.barh(wrapped_models, avg_cyclomatic_complexity_values, color='cyan')
# plt.xlabel('Complexidade Ciclomática Média')
# plt.ylabel('Modelo LLM')
# plt.tight_layout()
# plt.xticks(fontsize=24)
# plt.yticks(fontsize=24)

# Add labels
# for bar in bars:
#     plt.text(bar.get_width() - 5, bar.get_y() + bar.get_height()/2, f'{bar.get_width():.2f}', va='center', fontsize=24)

# plt.savefig('plots/sonar-metrics/avg_cyclomatic_complexity_per_llm.pdf')
# plt.close()