import os
import json
import time
import requests
from dotenv import load_dotenv
import asyncio

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

BASE_URL = "https://leetcode.com"
current_token_index = 1

def get_current_token():
    return {
        'leetcode_session': os.getenv(f'LEETCODE_SESSION{current_token_index}'),
        'csrf_token': os.getenv(f'csrftoken{current_token_index}')
    }

def rotate_token():
    global current_token_index
    current_token_index += 1
    if not os.getenv(f'LEETCODE_SESSION{current_token_index}') or not os.getenv(f'csrftoken{current_token_index}'):
        current_token_index = 1
    print(f'Rotating token. Now using LEETCODE_SESSION{current_token_index} and csrftoken{current_token_index}')

def validate_tokens():
    tokens = get_current_token()
    if not tokens['leetcode_session']:
        print("LEETCODE_SESSION is not defined. Please set the environment variable.")
        exit(1)
    if not tokens['csrf_token']:
        print("csrftoken is not defined. Please set the environment variable.")
        exit(1)

validate_tokens()

def delay(ms):
    time.sleep(ms / 1000)

def log(message):
    print(f'[{time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())}] {message}')

def graphql_headers(session, csrf_token):
    return {
        "content-type": "application/json",
        "origin": BASE_URL,
        "referer": BASE_URL,
        "cookie": f'csrftoken={csrf_token}; LEETCODE_SESSION={session};',
        "x-csrftoken": csrf_token,
    }

async def execute_graphql_request(url, headers, graphql):
    max_retries = 3
    retry_delay = lambda retry_count: 2 ** retry_count * 1000

    for attempt in range(max_retries):
        try:
            response = requests.post(url, headers=headers, data=graphql)
            result = response.json()
            if 'errors' in result:
                print("GraphQL errors:", result['errors'])
                return None
            return result['data']
        except Exception as error:
            print(f'Attempt {attempt + 1} failed:', error)
            if attempt < max_retries - 1:
                print(f'Retrying in {retry_delay(attempt)}ms...')
                await asyncio.sleep(retry_delay(attempt) / 1000)
            else:
                print("Max retries reached. Request failed.")
                rotate_token()
                validate_tokens()
                return "TIME OUT!"

async def get_question_id(title_slug):
    log(f'Getting question details for titleSlug: {title_slug}...')
    tokens = get_current_token()
    headers = graphql_headers(tokens['leetcode_session'], tokens['csrf_token'])
    graphql = json.dumps({
        "query": "query questionId($titleSlug: String!) { question(titleSlug: $titleSlug) { questionId } }",
        "variables": {"titleSlug": title_slug},
        "operationName": "questionId"
    })
    result = await execute_graphql_request("https://leetcode.com/graphql/", headers, graphql)
    if not result or 'question' not in result:
        print("Unexpected response format or no question found:", result)
        return None
    return result['question']

async def interpret_solution(problem_slug, question_id, typed_code, data_input, language="python3"):
    tokens = get_current_token()
    url = f'{BASE_URL}/problems/{problem_slug}/interpret_solution/'
    headers = {
        "content-type": "application/json",
        "origin": BASE_URL,
        "referer": f'{BASE_URL}/problems/{problem_slug}/',
        "x-csrftoken": tokens['csrf_token'],
        "cookie": f'LEETCODE_SESSION={tokens["leetcode_session"]}; csrftoken={tokens["csrf_token"]};',
        "User-Agent": "curl/8.0.1",
        "Accept": "*/*"
    }
    body = json.dumps({
        "lang": language,
        "question_id": question_id,
        "typed_code": typed_code,
        "data_input": data_input
    })
    max_retries = 3
    retry_delay = lambda retry_count: 5 ** retry_count * 1000

    for attempt in range(max_retries):
        try:
            response = requests.post(url, headers=headers, data=body)
            if response.status_code == 403:
                raise Exception("Forbidden: You don't have permission to access this resource. interpret_solution route")
            elif response.status_code == 429:
                raise Exception("Too Many Requests: You have sent too many requests in a given amount of time. interpret_solution route")
            result = response.json()
            if 'errors' in result:
                print("Errors:", result['errors'])
                return None
            return result
        except Exception as error:
            print('Error:', error)
            if ("Too Many Requests" in str(error) or "Forbidden" in str(error)) and attempt < max_retries - 1:
                print(f'Retrying in {retry_delay(attempt)}ms...')
                await asyncio.sleep(retry_delay(attempt) / 1000)
            else:
                if "Forbidden" in str(error):
                    error_response = {"response": True, "status": "error"}
                    print("Saving error response:", error_response)
                    return error_response
                rotate_token()
                validate_tokens()
                return None

async def check_submission_status(problem_slug, interpret_id):
    tokens = get_current_token()
    url = f'{BASE_URL}/submissions/detail/{interpret_id}/check/'
    headers = {
        "content-type": "application/json",
        "referer": f'{BASE_URL}/problems/{problem_slug}/submissions',
        "x-csrftoken": tokens['csrf_token'],
        "cookie": f'LEETCODE_SESSION={tokens["leetcode_session"]}; csrftoken={tokens["csrf_token"]};',
        "User-Agent": "curl/8.0.1",
        "Accept": "*/*"
    }
    try:
        response = requests.get(url, headers=headers)
        result = response.json()
        if 'errors' in result:
            print("Errors:", result['errors'])
            return None
        return result
    except Exception as error:
        print("Error:", error)
        return None

async def get_console_panel_config(title_slug):
    log(f'Getting console panel config for titleSlug: {title_slug}...')
    tokens = get_current_token()
    headers = graphql_headers(tokens['leetcode_session'], tokens['csrf_token'])
    graphql = json.dumps({
        "query": "query consolePanelConfig($titleSlug: String!) { question(titleSlug: $titleSlug) { exampleTestcaseList } }",
        "variables": {"titleSlug": title_slug},
        "operationName": "consolePanelConfig"
    })
    result = await execute_graphql_request("https://leetcode.com/graphql/", headers, graphql)
    if not result or 'question' not in result:
        print("Unexpected response format or no question found:", result)
        return None
    return result['question']

def reset_incorrect_responses():
    data_incorrect_dir = os.path.join(os.path.dirname(__file__), 'data_incorrect')
    response_dir = os.path.join(data_incorrect_dir, 'response')
    os.makedirs(response_dir, exist_ok=True)
    llms = ['gpt-4', 'claude-3-haiku', 'llama-3.1', 'gemini']

    for llm in llms:
        incorrect_file_path = os.path.join(data_incorrect_dir, f'incorrect_questions_{llm}.json')
        new_file_path = os.path.join(response_dir, f'filteredDataToResponse_{llm}.json')

        with open(incorrect_file_path, 'r', encoding='utf8') as f:
            incorrect_data = json.load(f)

        for item in incorrect_data:
            item['response'] = False

        with open(new_file_path, 'w', encoding='utf8') as f:
            json.dump(incorrect_data, f, indent=2)
        log(f'Reset responses in JSON file for {llm}')

async def data_to_response_llm():
    data_incorrect_dir = os.path.join(os.path.dirname(__file__), 'data_incorrect')
    response_dir = os.path.join(data_incorrect_dir, 'response')

    response_data_dir = os.path.join(os.path.dirname(__file__), 'response')

    llms = ['gpt-4', 'claude-3-haiku', 'llama-3.1', 'gemini']

    for llm in llms:
        llm_file_path = os.path.join(response_dir, f'filteredDataToResponse_{llm}.json')
        with open(llm_file_path, 'r', encoding='utf8') as f:
            llm_data = json.load(f)
        llm_path = os.path.join(response_data_dir, llm)

        log("==========================================================")
        log(f'Processing LLM: {llm}')

        if os.path.isdir(llm_path):
            files = os.listdir(llm_path)
            total_files = len(files)
            processed_files = 0

            for file in files:
                file_path = os.path.join(llm_path, file)
                json_index = next((i for i, item in enumerate(llm_data) if item['fileName'] == file), -1)

                if json_index == -1:
                    file_id = file.split('_')[0]
                    json_index = next((i for i, item in enumerate(llm_data) if item['questionId'] == file_id), -1)

                if json_index == -1:
                    log(f'File {file} not found in JSON data. Skipping.')
                    continue

                if llm_data[json_index]['response'] != False:
                    log("==========================================================")
                    log(f'Skipping already processed file: {file}')
                    processed_files += 1
                    continue

                with open(file_path, 'r', encoding='utf8') as f:
                    typed_code = f.read().replace('\n', '\r\n')
                log("==========================================================")
                log(f'Processing file: {file}')

                question = await get_question_id(llm_data[json_index]['titleSlug'])
                if not question:
                    log(f'Failed to get question details for file: {file}')
                    continue

                console_panel_config = await get_console_panel_config(llm_data[json_index]['titleSlug'])
                if not console_panel_config:
                    log(f'Failed to get console panel config for file: {file}')
                    continue

                result = await interpret_solution(
                    llm_data[json_index]['titleSlug'],
                    question['questionId'],
                    typed_code,
                    '\n'.join(console_panel_config['exampleTestcaseList'])
                )

                if not result or 'interpret_id' not in result:
                    log(f'Failed to interpret solution for file: {file}')
                    continue

                log(f'Checking submission for submissionId: {result["interpret_id"]}...')
                await asyncio.sleep(5)

                interpret_id = result['interpret_id']
                submission_status = await check_submission_status(llm_data[json_index]['titleSlug'], interpret_id)

                if not submission_status:
                    log(f'Failed to check submission status for file: {file}')
                    continue

                if 'status_code' not in submission_status:
                    log(f'status_code not found in submission status for file: {file}')
                    continue

                status = 'error'
                if submission_status['status_code'] == 10:
                    if submission_status['total_correct'] == submission_status['total_testcases']:
                        status = 'success'
                    else:
                        status = 'incorrect'

                llm_data[json_index].update({
                    'response': True,
                    'status': status,
                    'details': submission_status
                })

                with open(llm_file_path, 'w', encoding='utf8') as f:
                    json.dump(llm_data, f, indent=2)
                log(f'Updated JSON file for {llm}: {file}')

                processed_files += 1
                log(f'Processed {processed_files}/{total_files} files for {llm}')
                await asyncio.sleep(5)

# Verificar se o diretório response existe
response_dir = os.path.join(os.path.dirname(__file__), 'data_incorrect', 'response')
if not os.path.exists(response_dir):
    reset_incorrect_responses()

# Chamar a função para processar as respostas
asyncio.run(data_to_response_llm())