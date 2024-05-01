import os
from langchain import PromptTemplate
from langchain.chains import LLMChain

from langchain.memory import ConversationBufferMemory

from langchain.chains import SequentialChain
import streamlit as st
import google.generativeai as genai


# Configure genai with the API key
genai.configure(api_key="") #Enter your API key here
# Create a generative model object
model = genai.GenerativeModel('gemini-pro')

# Store chat history
chat = model.chat_history = []

def get_gemini_response(question):
  """
  Sends a question to Gemini and returns the generated response.

  Args:
      question: The question to ask Gemini.

  Returns:
      The generated response from Gemini.
  """
  response = model.generate_content(question)
  st.write(f"AI: {response.text}")  # Extract text from the response object


def generate_world_seed(core_concept):
    """
    Generates descriptions of a world based on a core concept using Gemini.

    Args:
        core_concept: A string describing the core concept for the world (e.g., "floating islands").

    Returns:
        A dictionary containing generated descriptions for geographical features, flora and fauna, and natural resources.
    """
    prompts = {
        "geography": f"Describe the geographical features of a world with {core_concept}.",
        "flora_fauna": f"Describe the unique flora and fauna found in a world with {core_concept}.",
        "resources": f"Describe the natural resources available in a world with {core_concept}."
    }

    descriptions = {}
    for category, prompt in prompts.items():
        description = get_gemini_response(prompt)  # Call get_gemini_response for each category
        descriptions[category] = description

    return descriptions



st.title("AI-powered World Builder")
st.write("Ask questions about your world concept and see what Gemini AI generates.")

user_question = st.text_input("Enter your world concept:")

if user_question:
    world_descriptions = generate_world_seed(user_question)

    st.write("Geographical Features:")
    x = st.write(world_descriptions.get("geography", "No description available"))

    st.write("\nFlora and Fauna:")
    y = st.write(world_descriptions.get("flora_fauna", "No description available"))

    st.write("\nNatural Resources:")
    z = st.write(world_descriptions.get("resources", "No description available"))
    
def generate_cultural_tapestry(societal_structure): #this function helps in developing the general  culture of the society
  """
  Generates descriptions of a culture based on a societal structure using Gemini.

  Args:
      societal_structure: A string describing the societal structure (e.g., "feudal").

  Returns:
      A dictionary containing generated descriptions for customs, traditions, religions, and rudimentary language.
  """
  prompts = {
    "customs": f"Describe some of the common customs and rituals practiced in a {societal_structure} society, especially considering the {x} and {y} and {z}.",
    "traditions": f"Describe some of the important traditions passed down through generations in a {societal_structure} society, reflecting their way of life in the {x} with {y} and {z}.",
    "religions": f"Describe the dominant religion or belief system in a {societal_structure} society, considering how it might be influenced by the {x} and {y} and {z}.",
    "language": f"Describe a few basic greetings and phrases in a rudimentary language used in a {societal_structure} society, perhaps reflecting elements of their environment like the {x} or {y} and {z}.",
    }

  descriptions = {}
  for category, prompt in prompts.items():
    description = get_gemini_response(prompt)  # Use the get_gemini_response function
    descriptions[category] = description

  return descriptions
    
user_structure = st.text_input("Enter a societal structure (e.g., feudal):")

if user_structure:
  cultural_tapestry = generate_cultural_tapestry(user_structure)

if user_structure:
  # Extract relevant details from world_descriptions
  world_geography = world_descriptions.get("geography", "")
  world_climate = world_descriptions.get("climate", "")

  # Call generate_cultural_tapestry with extracted details
  cultural_tapestry = generate_cultural_tapestry(user_structure, world_geography, world_climate)

  st.write("World Details:")
  # Loop through and display generated world descriptions
  for category, description in world_descriptions.items():
    st.write(f"{category.title()}: {description}")  # Display category title and description
