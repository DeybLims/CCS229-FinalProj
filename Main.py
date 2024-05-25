import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=os.getenv("API_KEY"))


if 'chat_session' not in st.session_state:
    model = genai.GenerativeModel('gemini-1.5-pro')  
    st.session_state.chat_session = model.start_chat()
    st.session_state.chat_history = []  


def handle_chat(question):
    try:
        response = st.session_state.chat_session.send_message(question)
        st.session_state.chat_history.append({"type": "Question", "content": question})
        st.session_state.chat_history.append({"type": "Response", "content": response.text})
        return response
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        return None


def story_creation_form():
    with st.form(key='story_form'):
        theme = st.text_input("What is the main idea or theme of the story? (e.g., love, betrayal, courage)")
        setting = st.text_input("What is the Setting of the story?")
        characters = st.text_input("Who are the Characters?")
        conflict = st.text_input("What is the main conflict or problem the characters face?")
        outcome = st.text_input("What is the outcome for the main characters?")
        submit_button = st.form_submit_button(label='Create Story')

        if submit_button:
            story_prompt = f"Write a story with the theme of {theme}, set in {setting}, with characters {characters}. The main conflict is {conflict} and it ends with {outcome}."
            return story_prompt
    return None


st.set_page_config(page_title="Story Creation Demo")
st.header("📚 Story Creation with Gemini")


story_prompt = story_creation_form()
if story_prompt:
    response = handle_chat(story_prompt)
    if response:
        st.subheader("Generated Story:")
        st.write(response.text)  


if 'chat_history' in st.session_state:
    st.subheader("Conversation History:")
    for entry in st.session_state.chat_history:
        if entry['type'] == "Question":
            st.markdown(f"*You asked:* {entry['content']}")
        elif entry['type'] == "Response":
            st.markdown(f"*Gemini replied:* {entry['content']}")

if st.button("Reset Conversation"):
    model = genai.GenerativeModel('gemini-1.5-pro')
    st.session_state.chat_session = model.start_chat()
    st.session_state.chat_history = []  # Clear history when resetting
