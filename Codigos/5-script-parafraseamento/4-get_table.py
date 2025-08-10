import os
import json
import csv

def calculate_assertivity_rate_and_save_to_csv():
    data_incorrect_dir = os.path.join(os.path.dirname(__file__), 'data_incorrect')
    response_dir = os.path.join(data_incorrect_dir, 'response')

    total_responses = 0
    successful_responses = 0
    correct_responses = 0
    incorrect_responses = 0
    error_responses = 0

    # Get all LLM files dynamically
    llm_files = [f for f in os.listdir(response_dir) if f.startswith('filteredDataToResponse_') and f.endswith('.json')]
    llms = [f.split('_')[1].rsplit('.', 1)[0] for f in llm_files]

    results = []

    for llm in llms:
        llm_file_path = os.path.join(response_dir, f'filteredDataToResponse_{llm}.json')
        if not os.path.exists(llm_file_path):
            print(f'File not found: {llm_file_path}')
            continue

        with open(llm_file_path, 'r', encoding='utf8') as f:
            llm_data = json.load(f)

        llm_total_responses = 0
        llm_successful_responses = 0
        llm_correct_responses = 0
        llm_incorrect_responses = 0
        llm_error_responses = 0

        for item in llm_data:
            if 'response' in item and item['response']:
                llm_total_responses += 1
                if item.get('status') == 'success':
                    llm_successful_responses += 1
                    if item.get('correct_answer') == True:
                        llm_correct_responses += 1
                    elif item.get('correct_answer') == False:
                        llm_incorrect_responses += 1
                else:
                    llm_error_responses += 1

        if llm_total_responses > 0:
            llm_assertivity_rate = (llm_successful_responses / llm_total_responses) * 100
            results.append([llm, llm_total_responses, llm_successful_responses, llm_correct_responses, llm_incorrect_responses, llm_error_responses, llm_assertivity_rate])
            total_responses += llm_total_responses
            successful_responses += llm_successful_responses
            correct_responses += llm_correct_responses
            incorrect_responses += llm_incorrect_responses
            error_responses += llm_error_responses

    if total_responses == 0:
        print("No responses found.")
        return

    overall_assertivity_rate = (successful_responses / total_responses) * 100
    print(f'Overall Assertivity Rate: {overall_assertivity_rate:.2f}%')

    # Save results to CSV
    csv_file_path = os.path.join(response_dir, 'assertivity_rates.csv')
    with open(csv_file_path, 'w', newline='', encoding='utf8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['LLM', 'Total Responses', 'Successful Responses', 'Correct Responses', 'Incorrect Responses', 'Error Responses', 'Assertivity Rate'])
        csvwriter.writerows(results)
        csvwriter.writerow(['Overall', total_responses, successful_responses, correct_responses, incorrect_responses, error_responses, overall_assertivity_rate])

if __name__ == "__main__":
    calculate_assertivity_rate_and_save_to_csv()