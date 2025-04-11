import streamlit as st
import requests

# Hugging Face API setup
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
headers = {
    "Authorization": f"Bearer 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"  # 👈 Your real token here
}

# Call Mistral API
def call_mistral(prompt):
    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code != 200:
        return f"Error {response.status_code}: {response.text}"
    result = response.json()
    return result[0]["generated_text"] if isinstance(result, list) else "Unexpected response"

# Streamlit App
st.title("Prince Kaka Chatbolt")
st.subheader("Ask me anything!")

# Session state for chat history
if "history" not in st.session_state:
    st.session_state.history = []

# Display chat history
for user_message, bot_message in st.session_state.history:
    st.write(f"**You:** {user_message}")
    st.write(f"**Bot:** {bot_message}")

# User input
user_input = st.text_input("You: ", key="input")

# Respond when the user submits a message
if user_input:
    # Build prompt from conversation history
    prompt = "You are a helpful assistant.\n"
    for user, bot in st.session_state.history:
        prompt += f"User: {user}\nAssistant: {bot}\n"
    prompt += f"User: {user_input}\nAssistant:"
    
    # Get response from Mistral
    bot_response = call_mistral(prompt)

    # Save conversation in session state
    st.session_state.history.append((user_input, bot_response))

    # Display the latest conversation
    st.write(f"**You:** {user_input}")
    st.write(f"**Bot:** {bot_response}")
