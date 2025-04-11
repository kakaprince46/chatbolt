import requests

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
headers = {
    "Authorization": f"Bearer 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"  # ← Replace this with your actual token
}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    
    # Check for errors
    if response.status_code != 200:
        print(f"Error {response.status_code}: {response.text}")
        return None

    return response.json()

# Your prompt
prompt = "Q: What is the capital of Nigeria?\nA:"

# Send the query
result = query({
    "inputs": prompt,
})

# Check and print result
if result:
    if isinstance(result, list) and "generated_text" in result[0]:
        print(result[0]["generated_text"])
    else:
        print("Unexpected response format:", result)
