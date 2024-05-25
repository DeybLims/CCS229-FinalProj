import streamlit as st
import os
from google.generativeai import genai
from dotenv import load_dotenv

# Load API key from environment variable
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=os.getenv("API_KEY"))
  # Ensure correct API key variable usage

# Initialize the chat session and chat history if not already present
if 'chat_session' not in st.session_state:
    model = genai.GenerativeModel('gemini-1.5-pro')  # Ensure consistent model version usage
    st.session_state.chat_session = model.start_chat()
    st.session_state.chat_history = []  # Initialize chat history here to avoid attribute error

# Function to handle chat interaction
def handle_chat(question):
    try:
        # Send the user's question to Gemini and fetch the response
        response = st.session_state.chat_session.send_message(question)
        # Append both question and response to the chat history
        st.session_state.chat_history.append({"type": "Question", "content": question})
        st.session_state.chat_history.append({"type": "Response", "content": response.text})
        return response
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
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
            # Optionally, display chat history
            st.subheader("Conversation History:")
            for entry in st.session_state.chat_history:
                if entry['type'] == "Question":
                    st.markdown(f"*You asked:* {entry['content']}")
                elif entry['type'] == "Response":
                    st.markdown(f"*Gemini replied:* {entry['content']}")
    else:
        st.warning("Please enter a question.")

if st.button("Reset Conversation"):
    # Restart the chat session if needed and clear the history
    model = genai.GenerativeModel('gemini-pro')  # Ensure consistent model version usage
    st.session_state.chat_session = model.start_chat()
    st.session_state.chat_history = []  # Clear history when resetting
