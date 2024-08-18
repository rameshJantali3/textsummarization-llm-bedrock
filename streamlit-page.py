import streamlit as st
import json
import requests
import re

# API endpoint
API_URL = "https://lambda api link "  # Replace with the actual API URL

def get_api_response(prompt):
    """Function to get response from the API"""
    payload = {
        'prompt': prompt
    }
    try:
        response = requests.post(API_URL, json=payload)
        print(response)
        response.raise_for_status()  # Check for HTTP errors
        response_json = response.json()
        body_content = response_json.get('body')
        nested_json = json.loads(body_content)
        generation_text = nested_json.get('generation', '')
        return (generation_text)
      
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# Streamlit UI
st.title("Text Summarization - Meta Llama 3 (Langauge Model)")

# Input field for search
prompt = st.text_input("Enter your prompt:")

if st.button("Search"):
    if prompt:

        api_response = get_api_response(prompt)

        if 'error' in api_response:
            st.error(f"Error: {api_response['error']}")
        else:
            st.write(api_response)
    else:
        st.warning("Please enter a prompt before searching.")
