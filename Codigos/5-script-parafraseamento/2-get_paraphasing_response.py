import os
import json
import time
import warnings
import logging
import nltk
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from g4f.client import Client
from g4f.cookies import set_cookies
from g4f.errors import RetryProviderError
from aiohttp.client_exceptions import ClientResponseError, ClientConnectorError

# Suppress TensorFlow logs
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# Suppress specific warnings
warnings.filterwarnings("ignore", category=UserWarning, message=".*Some weights of PegasusForConditionalGeneration were not initialized.*")
warnings.filterwarnings("ignore", category=UserWarning, message=".*Attempting to register factory for plugin.*")
warnings.filterwarnings("ignore", category=UserWarning, message=".*You should probably TRAIN this model on a down-stream task.*")

# Configure logging
logging.getLogger("transformers").setLevel(logging.ERROR)
logging.getLogger("tensorflow").setLevel(logging.ERROR)
logging.getLogger("transformers.modeling_utils").setLevel(logging.ERROR)

# Download the punkt tokenizer data
nltk.download('punkt')

# Initialize the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("tuner007/pegasus_paraphrase", use_fast=False)
model = AutoModelForSeq2SeqLM.from_pretrained("tuner007/pegasus_paraphrase")

# Initialize the pipeline
nlp = pipeline("text2text-generation", model=model, tokenizer=tokenizer, truncation=True)

client = Client()

# List of LLMs
llms = ['gpt-4', 'claude-3-haiku', 'llama-3.1', 'gemini']

def log(message):
    print(f"[{time.strftime('%a, %d %b %Y %H:%M:%S GMT', time.gmtime())}] {message}")

def paraphrase_message(message):
    sentences = nltk.sent_tokenize(message)
    paraphrased_sentences = []
    for sentence in sentences:
        paraphrased = nlp(sentence)[0]['generated_text']
        paraphrased_sentences.append(paraphrased)
    paraphrased_message = " ".join(paraphrased_sentences)
    return paraphrased_message

def chat_completion(problem, classMethodDefinition, model):
    message = f'''Generate only the PYTHON code for the following problem: {problem}

    Ensure that the function has the same name and the same number of parameters as in this example: {classMethodDefinition}

    If the example does not provide it, always start the code with "class Solution" followed by the function.

    Important!!! Only use the "class Solution". Do not create another class!!! and do not use any libraries!!!. I want only the PYTHON code, no texts!!!, no comments!!!
    '''
    
    # Separate the part to be paraphrased
    part_to_paraphrase = f'''Generate only the PYTHON code for the following problem: {problem}

    Ensure that the function has the same name and the same number of parameters as in this example:
    '''
    
    # Paraphrase the message
    paraphrased_part = paraphrase_message(part_to_paraphrase)
    
    # Recombine the message
    final_message = f"{paraphrased_part} {classMethodDefinition}\n\nIf the example does not provide it, always start the code with \"class Solution\" followed by the function.\n\nImportant!!! Only use the \"class Solution\". Do not create another class!!! and do not use any libraries!!!. I want only the PYTHON code, no texts!!!, no comments!!!"
    
    retries = 5
    wait_time = 5  # initial wait time in seconds
    for attempt in range(retries):
        try:
            chat_completion = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": final_message}],
            )
            response = chat_completion.choices[0].message.content or ""
            return response, message, final_message
        except (RetryProviderError, ClientResponseError, ClientConnectorError) as e:
            log(f"Attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                time.sleep(wait_time)
                wait_time *= 2  # exponential backoff
            else:
                raise

# Processar arquivos JSON de questões incorretas
incorrect_dir = './data_incorrect'

for llm in llms:
    log(f"Processing model {llm}")
    incorrect_file_path = os.path.join(incorrect_dir, f'incorrect_questions_{llm}.json')
    
    if not os.path.exists(incorrect_file_path):
        log(f"File {incorrect_file_path} not found.")
        continue

    with open(incorrect_file_path, 'r') as file:
        incorrect_data = json.load(file)

    for index, item in enumerate(incorrect_data):
        if not item.get('response'):
            response = ""
            attempts = 0
            while not response and attempts < 3:
                response, message, paraphrased_message = chat_completion(item['question'], item['classAndMethodDefinition'], llm)
                if not response.strip():
                    log(f"Empty response for ({index + 1}/{len(incorrect_data)}) {item['fileName']}, trying again...")
                    time.sleep(5) # Wait 5 seconds before trying again
                    attempts += 1

            if not response.strip():
                log(f"Skipping ({index + 1}/{len(incorrect_data)}) {item['fileName']} due to empty response after 3 attempts.")
                continue

            lines = response.splitlines()
            cleaned_text = "\n".join(lines[1:-1])

            if not os.path.exists('response'):
                os.mkdir('response')

            if not os.path.exists(f"./response/{llm}/"):
                os.mkdir(f"./response/{llm}/")

            file_name = f"./response/{llm}/{item['fileName']}"
            
            # Retry logic for empty file or missing "class Solution"
            for retry in range(3):
                with open(file_name, "w") as f:
                    f.write(cleaned_text)
                
                if os.path.getsize(file_name) == 0 or not cleaned_text.startswith("class Solution"):
                    log(f"Retry {retry + 1}: Invalid response for ({index + 1}/{len(incorrect_data)}) {item['fileName']}, trying again...")
                    response, message, paraphrased_message = chat_completion(item['question'], item['classAndMethodDefinition'], llm)
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
            item['fileName'] = f"{item['fileName']}"

            # Mark the item as processed
            item['response'] = True

            # Save the message and paraphrased_message
            item['message'] = message
            item['paraphrased_message'] = paraphrased_message

            with open(incorrect_file_path, 'w') as file:
                json.dump(incorrect_data, file, indent=4)
            
            log(f"({index + 1}/{len(incorrect_data)}) {item['fileName']} PROCESSED!")
            time.sleep(5)

log("All items have been processed and updated.")