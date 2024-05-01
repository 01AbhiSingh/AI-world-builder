---

# AI-powered World Builder

## Overview

This project is an AI-powered World Builder that leverages the Gemini AI model to generate descriptions for various aspects of a fictional world, including geographical features, flora and fauna, natural resources, customs, traditions, religions, and rudimentary language based on user input.

## Features

- **World Generation:** Enter a world concept, and the AI generates descriptions for geographical features, flora and fauna, and natural resources.
- **Cultural Tapestry:** Define a societal structure, and the AI generates descriptions for customs, traditions, religions, and rudimentary language reflecting that structure.
- **Character Generation:** Generate new characters on the basis of the previous information generated.
## Usage

1. **Install Dependencies:**
   - Make sure you have Python installed on your system.
   - Install required Python packages using `pip install -r requirements.txt`.

2. **Run the Application:**
   - Execute `streamlit run app.py` to launch the Streamlit application locally.

3. **Interact with the AI:**
   - Enter your world concept in the text input field.
   - Receive generated descriptions for geographical features, flora and fauna, and natural resources.
   - Enter a societal structure in the text input field.
   - Receive generated descriptions for customs, traditions, religions, and rudimentary language reflecting that structure.

## Dependencies

- `os`
- `streamlit`
- `google.generativeai`

## Configuration

- Obtain an API key from Google's Generative AI platform and replace `YOUR_API_KEY` with your actual API key in `genai.configure(api_key="YOUR_API_KEY")`.

## Notes

- This project is for demonstration purposes only and may require additional customization for production use.

## Contributors

- [Abhishek Singh](link to your profile)

---
