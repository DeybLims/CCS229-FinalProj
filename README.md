
# Story Creation with Gemini

This project leverages Google's generative AI, specifically the Gemini model, to create dynamic stories based on user inputs. Built using Streamlit, this app provides a simple and interactive interface to generate stories by specifying elements such as theme, setting, characters, conflict, and outcome.

## Project Setup

### Prerequisites

- Python 3.8+
- Pip
- An API key from Google Cloud with access to the Gemini model

### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://yourrepository.git
   cd yourrepository
   ```

2. **Set up a Virtual Environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**
   ```bash
   pip install streamlit google-generativeai python-dotenv
   ```

4. **Environment Variables:**
   - Create a `.env` file in the root directory of the project.
   - Add your API key to the `.env` file:
     ```plaintext
     GEMINI_API_KEY='your_api_key_here'
     ```

### Running the Application

Execute the following command to run the app:
```bash
streamlit run your_script_name.py
```

## Functionalities

- **Story Creation:** Users can create a story by filling out a form that captures the theme, setting, characters, conflict, and desired outcome of the story.

- **Dynamic Interaction:** The app interacts with Google's Gemini AI to generate stories based on the specified inputs.

- **Conversation History:** Displays a history of the questions asked and the stories generated, allowing users to see a log of their interactions.

- **Reset Functionality:** Users can reset the conversation, clearing all history and starting afresh.

## Usage Instructions

1. **Open the App:**
   - Start the app and navigate to the provided local URL (usually `http://localhost:8501`).

2. **Input Story Elements:**
   - Enter the desired elements of your story in the provided text fields.

3. **Generate the Story:**
   - Click the 'Create Story' button to submit your inputs. The app will communicate with Gemini AI to generate a story based on your inputs.

4. **View the Generated Story and History:**
   - The generated story will appear under the 'Generated Story' section.
   - Scroll through the 'Conversation History' to review past interactions.

5. **Reset Conversation:**
   - Use the 'Reset Conversation' button to clear all previous interactions and start a new session.

## Troubleshooting

- **API Key Issues:** Ensure that your API key is correctly entered in the `.env` file and that it has not expired or been restricted.

- **Connectivity:** Check your internet connection if the app fails to communicate with Google's Gemini API.

## Contributing

Contributions to enhance the functionalities or improve the design of this app are welcome. Please adhere to conventional coding practices and open a pull request for changes.

## License

Specify your license or leave it as default to no license.

---

For more information, visit [Streamlit Documentation](https://docs.streamlit.io) or [Google's API Documentation](https://cloud.google.com/apis/docs/overview).
