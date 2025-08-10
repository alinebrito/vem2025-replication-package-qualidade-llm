import os
import json

def process_json_files():
    # Listar todos os arquivos JSON na pasta response
    response_dir = './response'
    data_dir = './data'
    output_dir = './data_incorrect'
    
    # Criar a pasta data_incorrect se não existir
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    json_files = [f for f in os.listdir(response_dir) if f.endswith('.json')]

    # Filtrar arquivos que começam com 'filteredDataToResponse_'
    filtered_files = [f for f in json_files if f.startswith('filteredDataToResponse_')]

    for filtered_file in filtered_files:
        # Nome do arquivo correspondente que começa com 'dataToResponse_'
        base_name = filtered_file.replace('filteredDataToResponse_', '')
        data_file = f'dataToResponse_{base_name}'

        if data_file not in os.listdir(data_dir):
            print(f'Arquivo correspondente {data_file} não encontrado para {filtered_file}')
            continue

        # Abrir arquivos JSON
        with open(os.path.join(response_dir, filtered_file), 'r') as f:
            filtered_data = json.load(f)
        
        with open(os.path.join(data_dir, data_file), 'r') as f:
            data = json.load(f)

        # Array para armazenar questões incorretas
        incorrect_questions = []

        # Percorrer elementos do array no arquivo filteredDataToResponse_
        for item in filtered_data:
            if item.get('status') == 'incorrect':
                # Pegar os atributos question e classAndMethodDefinition do elemento correspondente no arquivo dataToResponse_
                question_data = next((d for d in data if d['questionId'] == item['questionId']), None)
                if question_data:
                    incorrect_questions.append({
                        'questionId': item['questionId'],
                        'fileName': item['fileName'],
                        'question': question_data.get('question'),
                        'titleSlug': question_data.get('titleSlug'),
                        'classAndMethodDefinition': question_data.get('classAndMethodDefinition')
                    })

        # Salvar questões incorretas em um novo arquivo JSON na pasta data_incorrect
        output_file = os.path.join(output_dir, f'incorrect_questions_{base_name}')
        with open(output_file, 'w') as f:
            json.dump(incorrect_questions, f, indent=4)

        print(f'Questões incorretas salvas em {output_file}')

if __name__ == "__main__":
    process_json_files()