import os
import json

# Lista de LLMs
llms = ['gpt-4', 'claude-3-haiku', 'gemini', 'llama-3.1']

# Caminho do arquivo de origem
source_file_path = './data/dataUpdatedWithSolutions.json'

# Verificar e criar arquivos JSON para cada LLM
for llm in llms:
    file_path = f'./data/dataToResponse_{llm}.json'
    if not os.path.exists(file_path):
        with open(source_file_path) as f:
            data = json.load(f)

        new_data = []

        for item in data:
            question_id = item.get('stat').get('question_id')
            title_slug = item.get('stat').get('question__title_slug')
            question = item.get('additionalData').get('question')
            classAndMethodDefinition = item.get('classAndMethodDefinition')
            
            new_item = {
                "questionId": question_id,
                "titleSlug": title_slug,
                "question": question,
                "classAndMethodDefinition": classAndMethodDefinition,
                "fileName": "",
                "response": False
            }
            new_data.append(new_item)

        # Salvar os dados extraídos em um novo arquivo JSON
        with open(file_path, 'w') as f:
            json.dump(new_data, f, indent=4)

        print(f"Arquivo {file_path} criado com sucesso.")
    else:
        print(f"Arquivo {file_path} já existe.")