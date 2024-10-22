# import os
# import json
# from concurrent.futures import ThreadPoolExecutor, as_completed

# # Function to convert a single JSON file to JSONL
# def convert_json_to_jsonl(json_file, jsonl_file):
#     try:
#         # Open the JSON file and load the data
#         with open(json_file, 'r', encoding='utf-8') as infile:
#             data = json.load(infile)

#         # Write to the output JSONL file
#         with open(jsonl_file, 'w', encoding='utf-8') as outfile:
#             # If the JSON data is a list, write each element as a separate line
#             if isinstance(data, list):
#                 for item in data:
#                     outfile.write(json.dumps(item) + '\n')
#             else:
#                 # If it's not a list, write it directly
#                 outfile.write(json.dumps(data) + '\n')

#         print(f"Successfully converted {json_file} to {jsonl_file}")

#     except Exception as e:
#         print(f"Error converting {json_file}: {e}")

# # Function to process all JSON files in a folder concurrently
# def batch_convert_json_to_jsonl(input_folder, output_folder, max_workers=4):
#     # Make sure the output folder exists, or create it
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)

#     # Get a list of all JSON files in the input folder
#     json_files = [f for f in os.listdir(input_folder) if f.endswith(".json")]

#     # Use ThreadPoolExecutor for parallel processing
#     with ThreadPoolExecutor(max_workers=max_workers) as executor:
#         # List to store futures (tasks that are running concurrently)
#         futures = []

#         # Loop through each file and submit the conversion task to the executor
#         for filename in json_files:
#             json_file = os.path.join(input_folder, filename)
#             jsonl_file = os.path.join(output_folder, filename.replace(".json", ".jsonl"))

#             # Submit the task for parallel processing
#             futures.append(executor.submit(convert_json_to_jsonl, json_file, jsonl_file))

#         # Wait for all futures (tasks) to complete
#         for future in as_completed(futures):
#             future.result()  # We can retrieve the result or just ensure it's completed

# # Example usage: Replace these paths with the actual folder paths on your system
# input_folder = 'C:/Users/salau/OneDrive - Michigan State University/CMSE_802/Project/1'   # Input folder with JSON files
# output_folder = 'C:/Users/salau/OneDrive - Michigan State University/CMSE_802/Project/converted_1' # Output folder for JSONL files

# # Run the batch conversion with parallelization (you can adjust the number of threads)
# batch_convert_json_to_jsonl(input_folder, output_folder, max_workers=8)


# import os
# import json
# from concurrent.futures import ThreadPoolExecutor, as_completed

# # Function to convert JSON to JSONL (same as before)
# def convert_json_to_jsonl(json_file, jsonl_file):
#     try:
#         with open(json_file, 'r', encoding='utf-8') as infile:
#             data = json.load(infile)

#         with open(jsonl_file, 'w', encoding='utf-8') as outfile:
#             if isinstance(data, list):
#                 for item in data:
#                     outfile.write(json.dumps(item) + '\n')
#             else:
#                 outfile.write(json.dumps(data) + '\n')

#         print(f"Successfully converted {json_file} to {jsonl_file}")

#     except Exception as e:
#         print(f"Error converting {json_file}: {e}")

# # Function to process all JSON files in a folder concurrently
# def batch_convert_json_to_jsonl(input_folder, output_folder, max_workers=4):
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)

#     json_files = [f for f in os.listdir(input_folder) if f.endswith(".json")]

#     with ThreadPoolExecutor(max_workers=max_workers) as executor:
#         futures = []
#         for filename in json_files:
#             json_file = os.path.join(input_folder, filename)
#             jsonl_file = os.path.join(output_folder, filename.replace(".json", ".jsonl"))
#             futures.append(executor.submit(convert_json_to_jsonl, json_file, jsonl_file))

#         for future in as_completed(futures):
#             future.result()

# # List of input folders
# input_folders = [
    # r'C:/Users/salau/OneDrive - Michigan State University/CMSE_802/Project/1',
    # r'C:/Users/salau/OneDrive - Michigan State University/CMSE_802/Project/2',
    # r'C:/Users/salau/OneDrive - Michigan State University/CMSE_802/Project/3',
    # r'C:/Users/salau/OneDrive - Michigan State University/CMSE_802/Project/4',
    # r'C:/Users/salau/OneDrive - Michigan State University/CMSE_802/Project/5',
    # r'C:/Users/salau/OneDrive - Michigan State University/CMSE_802/Project/6'
# ]

# # Base output directory
# output_base = r'C:/Users/salau/OneDrive - Michigan State University/CMSE_802/Project/'

# # Loop through each input folder and create a numbered output folder
# for i, input_folder in enumerate(input_folders, start=1):
#     output_folder = os.path.join(output_base, f'jsonl_output_folder_{i}')
#     batch_convert_json_to_jsonl(input_folder, output_folder, max_workers=8)




# import os
# import json
# from bs4 import BeautifulSoup
# from concurrent.futures import ThreadPoolExecutor, as_completed

# # Function to extract body text from content
# def extract_body_text(content):
#     try:
#         # Parse the HTML/XML content
#         soup = BeautifulSoup(content, 'html.parser')
#         # Extract the <bodyText> tag (adjust as necessary based on your content structure)
#         body_text = soup.find('bodytext')  # Adjust the tag to the appropriate one if necessary
#         return body_text.get_text(strip=True) if body_text else ""
#     except Exception as e:
#         print(f"Error extracting body text: {e}")
#         return ""

# # Function to convert JSON files to a single JSONL file for each folder
# def convert_json_to_jsonl(input_folder, output_file):
#     articles = []

#     # Process each JSON file in the input folder
#     json_files = [f for f in os.listdir(input_folder) if f.endswith(".json")]
    
#     for filename in json_files:
#         json_file_path = os.path.join(input_folder, filename)
#         try:
#             with open(json_file_path, 'r', encoding='utf-8') as infile:
#                 data = json.load(infile)

#                 # Ensure data is a dictionary before accessing keys
#                 if not isinstance(data, dict):
#                     print(f"Warning: {json_file_path} does not contain a valid JSON object.")
#                     continue

#                 # Extracting required fields; adjust keys based on your JSON structure
#                 date = data.get('date') or data.get('Date')  # Handles both lower and upper case
#                 title = data.get('title') or data.get('Title')  # Handles both lower and upper case
#                 source = data.get('source') or data.get('Source')  # Handles both lower and upper case
                
#                 # Handle the Document dictionary safely
#                 document = data.get('Document')
#                 if document is None:
#                     print(f"Warning: No Document found in {json_file_path}.")
#                     continue

#                 content = document.get('Content', "")
#                 body_text = extract_body_text(content)

#                 if body_text:  # Only add articles that have body text
#                     articles.append({
#                         'text': body_text,
#                         'meta': {
#                             'date': date,
#                             'title': title,
#                             'source': source
#                         }
#                     })

#         except Exception as e:
#             print(f"Error processing {json_file_path}: {e}")

#     # Write all articles to a single JSONL file
#     with open(output_file, 'w', encoding='utf-8') as outfile:
#         for article in articles:
#             outfile.write(json.dumps(article) + '\n')

#     print(f"Successfully converted files in {input_folder} to {output_file}")

# # Function to process all input folders concurrently
# def batch_convert_json_to_jsonl(input_folders, output_base, max_workers=4):
#     with ThreadPoolExecutor(max_workers=max_workers) as executor:
#         futures = []
#         for i, input_folder in enumerate(input_folders, start=1):
#             output_file = os.path.join(output_base, f'combined_output_{i}.jsonl')
#             futures.append(executor.submit(convert_json_to_jsonl, input_folder, output_file))

#         for future in as_completed(futures):
#             future.result()

# # Example usage
# input_folders = [
#     r'C:/Users/salau/OneDrive - Michigan State University/CMSE_802/Project/1',  # Change to your actual folder path
#     r'C:/Users/salau/OneDrive - Michigan State University/CMSE_802/Project/2',
#     r'C:/Users/salau/OneDrive - Michigan State University/CMSE_802/Project/3',
#     r'C:/Users/salau/OneDrive - Michigan State University/CMSE_802/Project/4',
#     r'C:/Users/salau/OneDrive - Michigan State University/CMSE_802/Project/5',
#     r'C:/Users/salau/OneDrive - Michigan State University/CMSE_802/Project/6'
    
# ]

# output_base = r'C:/Users/salau/OneDrive - Michigan State University/CMSE_802/Project/'  # Change to your desired output path

# batch_convert_json_to_jsonl(input_folders, output_base, max_workers=8)


import os
import json
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed

# Function to extract body text from content
def extract_body_text(content):
    try:
        # Parse the HTML/XML content
        soup = BeautifulSoup(content, 'html.parser')
        # Extract the <bodyText> tag (adjust as necessary based on your content structure)
        body_text = soup.find('bodytext')  # Adjust the tag to the appropriate one if necessary
        return body_text.get_text(strip=True) if body_text else ""
    except Exception as e:
        print(f"Error extracting body text: {e}")
        return ""

# Function to extract body text from Document or Extracts
def extract_full_body_text(data):
    body_text = ""

    # Check if Document is present and contains Content
    if 'Document' in data and data['Document'] is not None:
        content = data['Document'].get('Content', '')
        body_text += extract_body_text(content)  # Extract from Document if available

    # If Document is None or empty, check Extracts
    if not body_text and 'Extracts' in data and isinstance(data['Extracts'], list):
        for extract in data['Extracts']:
            if 'SummaryText' in extract:
                body_text += extract['SummaryText'] + " "  # Add summary texts

    return body_text.strip()  # Remove any leading/trailing whitespace

# Function to convert JSON files to a single JSONL file for each folder
def convert_json_to_jsonl(input_folder, output_file):
    articles = []

    # Process each JSON file in the input folder
    json_files = [f for f in os.listdir(input_folder) if f.endswith(".json")]
    
    for filename in json_files:
        json_file_path = os.path.join(input_folder, filename)
        try:
            with open(json_file_path, 'r', encoding='utf-8') as infile:
                data = json.load(infile)

                # Ensure data is a dictionary before accessing keys
                if not isinstance(data, dict):
                    print(f"Warning: {json_file_path} does not contain a valid JSON object.")
                    continue

                # Extracting required fields; adjust keys based on your JSON structure
                date = data.get('date') or data.get('Date')  # Handles both lower and upper case
                title = data.get('title') or data.get('Title')  # Handles both lower and upper case
                source = data.get('source') or data.get('Source')  # Handles both lower and upper case

                # Extract body text using the new helper function
                body_text = extract_full_body_text(data)

                if body_text:  # Only add articles that have body text
                    articles.append({
                        'text': body_text,
                        'meta': {
                            'date': date,
                            'title': title,
                            'source': source
                        }
                    })

        except Exception as e:
            print(f"Error processing {json_file_path}: {e}")

    # Write all articles to a single JSONL file
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for article in articles:
            outfile.write(json.dumps(article) + '\n')

    print(f"Successfully converted files in {input_folder} to {output_file}")

# Function to process all input folders concurrently
def batch_convert_json_to_jsonl(input_folders, output_base, max_workers=4):
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = []
        for i, input_folder in enumerate(input_folders, start=1):
            output_file = os.path.join(output_base, f'combined_output_{i}.jsonl')
            futures.append(executor.submit(convert_json_to_jsonl, input_folder, output_file))

        for future in as_completed(futures):
            future.result()

# Example usage
input_folders = [
    r'C:/Users/salau/OneDrive - Michigan State University/CMSE_802/Project/1',  # Change to your actual folder path
    r'C:/Users/salau/OneDrive - Michigan State University/CMSE_802/Project/2',
    r'C:/Users/salau/OneDrive - Michigan State University/CMSE_802/Project/3',
    r'C:/Users/salau/OneDrive - Michigan State University/CMSE_802/Project/4',
    r'C:/Users/salau/OneDrive - Michigan State University/CMSE_802/Project/5',
    r'C:/Users/salau/OneDrive - Michigan State University/CMSE_802/Project/6'
]

output_base = r'C:/Users/salau/OneDrive - Michigan State University/CMSE_802/Project/'  # Change to your desired output path

batch_convert_json_to_jsonl(input_folders, output_base, max_workers=8)

#prodigy db-out news_1 > annotations.jsonl

#prodigy train ner annotate_news_1 --output ./model_output --label RELEVANT

# prodigy stats annotate_news_1

 #prodigy train-curve --ner annotate_news_1 --show-plot
 #RESUME LATER
 #prodigy textcat.teach news_1 en_core_web_sm combined_output_1.jsonl --label RELEVANT

3097-2573-269A-B04A