import os
import json
import time
from g4f.client import Client
from g4f.cookies import set_cookies
from g4f.errors import RetryProviderError
from aiohttp.client_exceptions import ClientResponseError, ClientConnectorError

client = Client()

# List of LLMs
llms = ['gpt-4', 'claude-3-haiku', 'llama-3.1', 'gemini']

def log(message):
    print(f"[{time.strftime('%a, %d %b %Y %H:%M:%S GMT', time.gmtime())}] {message}")

def chat_completion(problem, classMethodDefinition, model):
    message = f'''
    Generate only the PYTHON code for the following problem: {problem}

    Ensure that the function has the same name and the same number of parameters as in this example: {classMethodDefinition}

    Important! Only use the "class Solution". Do not create another class and do not use any libraries. I want only the Python code with no texts and, no comments.
    '''
    retries = 5
    wait_time = 5  # initial wait time in seconds
    for attempt in range(retries):
        try:
            chat_completion = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": message}],
            )
            response = chat_completion.choices[0].message.content or ""
            return response
        except (RetryProviderError, ClientResponseError, ClientConnectorError) as e:
            log(f"Attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                time.sleep(wait_time)
                wait_time *= 2  # exponential backoff
            else:
                raise

for llm in llms:
    log(f"Processing model {llm}")
    json_file_path = f'./data/dataToResponse_{llm}.json'
    
    if not os.path.exists(json_file_path):
        log(f"File {json_file_path} not found.")
        continue

    with open(json_file_path, 'r') as file:
        data = json.load(file)

    for index, item in enumerate(data):
        if not item['response']:
            response = ""
            attempts = 0
            while not response and attempts < 3:
                response = chat_completion(item['question'], item['classAndMethodDefinition'], llm)
                if not response.strip():
                    log(f"Empty response for ({index + 1}/{len(data)}) {item['questionId']}_{item['titleSlug']}_{llm}.py, trying again...")
                    time.sleep(5) # Wait 5 seconds before trying again
                    attempts += 1

            if not response.strip():
                log(f"Skipping ({index + 1}/{len(data)}) {item['questionId']}_{item['titleSlug']}_{llm}.py due to empty response after 3 attempts.")
                continue

            lines = response.splitlines()
            cleaned_text = "\n".join(lines[1:-1])

            if not os.path.exists('response'):
                os.mkdir('response')

            if not os.path.exists(f"./response/{llm}/"):
                os.mkdir(f"./response/{llm}/")

            file_name = f"./response/{llm}/{item['questionId']}_{item['titleSlug']}_{llm}.py"
            
            # Retry logic for empty file or missing "class Solution"
            for retry in range(3):
                with open(file_name, "w") as f:
                    f.write(cleaned_text)
                
                if os.path.getsize(file_name) == 0 or not cleaned_text.startswith("class Solution"):
                    log(f"Retry {retry + 1}: Invalid response for ({index + 1}/{len(data)}) {item['questionId']}_{item['titleSlug']}_{llm}.py, trying again...")
                    response = chat_completion(item['question'], item['classAndMethodDefinition'], llm)
                    lines = response.splitlines()
                    cleaned_text = "\n".join(lines[1:-1])
                    time.sleep(5)
                else:
                    break
            else:
                if not cleaned_text.startswith("class Solution"):
                    cleaned_text = "class Solution:\n" + cleaned_text

            with open(file_name, "w") as f:
                f.write(cleaned_text)

            # Update the fileName attribute
            item['fileName'] = f"{item['questionId']}_{item['titleSlug']}_{llm}.py"

            # Mark the item as processed
            item['response'] = True

            with open(json_file_path, 'w') as file:
                json.dump(data, file, indent=4)
            
            log(f"({index + 1}/{len(data)}) {item['questionId']}_{item['titleSlug']}_{llm}.py PROCESSED!")
            time.sleep(5)

log("All items have been processed and updated.")