import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key from environment variable

load_dotenv()  # This loads the environment variables from a .env file.

api_key = os.getenv("GEMINI_API_KEY")

# Initialize the chat session
if 'chat_session' not in st.session_state:
    model = genai.GenerativeModel('gemini-pro', api_key=GEMINI_API_KEY)
    st.session_state.chat_session = model.start_chat()

# Function to handle chat interaction
def handle_chat(question):
    try:
        response = st.session_state.chat_session.send_message(question)
        st.session_state.chat_history.append({"type": "Question", "content": question})
        return response
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None


# Streamlit App setup
st.set_page_config(page_title="Dynamic Q&A Demo")
st.header("Dynamic Conversation with Gemini")

user_input = st.text_input("Your Question:", key="user_query")

if st.button("Ask Gemini"):
    if user_input:
        response = handle_chat(user_input)
        if response:
            st.subheader("Gemini's Response:")
            st.write(response.text)  # Assuming 'text' is the correct attribute; adjust as per the actual response structure
    else:
        st.warning("Please enter a question.")

if st.button("Reset Conversation"):
    # Restart the chat session if needed
    model = genai.GenerativeModel('gemini-pro')
    st.session_state.chat_session = model.start_chat()
