import requests
import sys

# Define the API URL and headers with your API key
API_URL = "https://api-inference.huggingface.co/models/mouadnech/Grammar-and-Spelling-Checker"
HEADERS = {"Authorization": "Bearer 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"}

# Function to query the model API with a given payload
def query(payload):
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    return response.json()


# Get the input sentence from the command line arguments
input_text = sys.argv[1]  # Input sentence from command-line arguments

# Query the model API with the input text
output = query({
    "inputs": input_text
})

# Extract the generated text from the API response
generated_text = output[0]["generated_text"]

# Print the generated text
print("Generated Sentence:")
print(generated_text)
