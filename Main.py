from google.oauth2 import service_account
from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Load API key from environment variable
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Specify the required scopes
SCOPES = ['https://www.googleapis.com/auth/cloud-platform']  # Adjust this based on actual requirements

# Load the service account credentials and specify the required scopes
credentials = service_account.Credentials.from_service_account_file(
    'service_account.json',
    scopes=SCOPES)

# Initialize the chat session and history
if 'chat_session' not in st.session_state:
    model = genai.GenerativeModel('gemini-pro')
    st.session_state.chat_session = model.start_chat()
    st.session_state.chat_history = []  # Initialize chat history

# Function to handle chat interaction
def handle_chat(question):
    try:
        # Send the user's question to Gemini and fetch the response
        response = st.session_state.chat_session.send_message(question)
        # Store the question and response in the history
        st.session_state.chat_history.append({"type": "Question", "content": question})
        st.session_state.chat_history.append({"type": "Response", "content": response.text})
        return response.text
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        return None

# Streamlit App setup
st.set_page_config(page_title="Dynamic Q&A Demo")
st.header("Dynamic Conversation with Gemini")

user_input = st.text_input("Your Question:", key="user_query")

if st.button("Ask Gemini"):
    if user_input:
        response_text = handle_chat(user_input)
        if response_text:
            st.subheader("Conversation History:")
            for entry in st.session_state.chat_history:
                if entry['type'] == "Question":
                    st.markdown(f"*You said:* {entry['content']}")
                elif entry['type'] == "Response":
                    st.markdown(f"*Gemini replied:* {entry['content']}")
    else:
        st.warning("Please enter a question.")

if st.button("Reset Conversation"):
    # Restart the chat session if needed and clear the history
    model = genai.GenerativeModel('gemini-pro')
    st.session_state.chat_session = model.start_chat()
    st.session_state.chat_history = []
