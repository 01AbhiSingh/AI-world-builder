from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.chains import SequentialChain
import streamlit as st
import google.generativeai as genai
import random
# Configure genai with the API key
genai.configure(api_key="")
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


def generate_geography(core_concept):
    """
    Describes the geographical features of a world based on the core concept.

    Args:
        core_concept (str): The core concept for the world.

    Returns:
        dict: A dictionary containing the description for geographical features.
    """

    prompt = f"Describe the geographical features of a world with {core_concept}."
    description = get_gemini_response(prompt)
    return {"geography": description}


def generate_flora_fauna(core_concept):
    """
    Describes the unique flora and fauna found in a world based on the core concept.

    Args:
        core_concept (str): The core concept for the world.

    Returns:
        dict: A dictionary containing the description for flora and fauna.
    """

    prompt = f"Describe the unique flora and fauna found in a world with {core_concept}."
    description = get_gemini_response(prompt)
    return {"flora_fauna": description}


def generate_resources(core_concept):
    """
    Describes the natural resources available in a world based on the core concept.

    Args:
        core_concept (str): The core concept for the world.

    Returns:
        dict: A dictionary containing the description for natural resources.
    """

    prompt = f"Describe the natural resources available in a world with {core_concept}."
    description = get_gemini_response(prompt)
    return {"resources": description}

def generate_cultural_tapestry(societal_structure, world_descriptions):
    """
    Generates descriptions of a culture based on a societal structure and world descriptions.

    Args:
        societal_structure (str): A string describing the societal structure (e.g., "feudal").
        world_descriptions (dict): A dictionary containing world descriptions (e.g., output from generate_world_description).

    Returns:
        dict: A dictionary containing generated descriptions for cultural aspects.
    """

    world_geography = world_descriptions.get("geography", "")
    world_climate = generate_geography(world_geography) 
    prompts = {
        "customs": f"Describe some of the common customs and rituals practiced in a {societal_structure} society, especially considering the {world_geography} and {world_climate}.",
        "traditions": f"Describe some of the important traditions passed down through generations in a {societal_structure} society, reflecting their way of life in the {world_geography} with {world_climate}.",
        "religions": f"Describe the dominant religion or belief system in a {societal_structure} society, considering how it might be influenced by the {world_geography} and {world_climate}.",
        "language": f"Describe a few basic greetings and phrases in a rudimentary language used in a {societal_structure} society, perhaps reflecting elements of their environment like the {world_geography} or {world_climate}.",
    }

    descriptions = {}
    for category, prompt in prompts.items():
        description = get_gemini_response(prompt)
        descriptions[category] = description

    return descriptions 

def generate_character(character_role, ethnicity):
    """
    Generates a character description based on a character role and ethnicity within the world.

    Args:
        character_role (str): The role of the character (e.g., "nomadic scholar").
        ethnicity (str): The ethnicity of the character within the world.

    Returns:
        dict: A dictionary containing generated descriptions for the character.
    """
    prompts = {
        "appearance": f"Describe the physical appearance of a {ethnicity} {character_role}.",
        "personality": f"Describe the personality and mannerisms of a {ethnicity} {character_role}.",
        "backstory": f"Describe the backstory and life experiences of a {ethnicity} {character_role}.",
        "skills": f"Describe the skills and abilities of a {ethnicity} {character_role}.",
        "aspirations": f"Describe the aspirations and goals of a {ethnicity} {character_role}."
    }

    descriptions = {}
    for category, prompt in prompts.items():
        description = get_gemini_response(prompt)
        descriptions[category] = description

    return descriptions

st.title("World Builder with Gemini")

core_concept_input = st.text_input("Enter a core concept for your world (e.g., floating islands):")

societal_structures = [
    "feudal",
    "egalitarian",
    "nomadic",
    "theocratic",
    "patriarchal",
    "matriarchal",
    "tribal",
    "democratic republic",
    "communist",
    "monarchy (absolute)",
    "monarchy (constitutional)",
    "oligarchy",
    "confederacy",
    "dictatorship",
    "gerontocracy",
    "hive mind",
    "technocracy",
    "nomadic city-state",
    "monarchy (absolute)",
    "monarchy (constitutional)",
    "monarchy (elective)",
    "oligarchy (aristocracy)",
    "oligarchy (plutocracy)",
    "oligarchy (timocracy)",
    "dictatorship (military junta)",
    "dictatorship (totalitarian)",
    "republic (democratic)",
    "republic (federal)",
    "republic (unitary)",
    "confederacy",
    "gerontocracy",
    "meritocracy",
    "theocracy",
    "technocracy",
    "anarchy",
    "capitalism (free market)",
    "capitalism (laissez-faire)",
    "socialism (democratic socialism)",
    "socialism (communist)",
    "barter system",
    "gift economy",
    "command economy",
    "resource-based economy (hunter-gatherer)",
    "resource-based economy (agrarian)",
    "sharing economy",
    "caste system",
    "class system (upper class)",
    "class system (middle class)",
    "class system (lower class)",
    "guild system",
    "egalitarian",
    "nuclear family",
    "extended family",
    "polygamy",
    "matriarchal",
    "patriarchal",
    "communal child-rearing",
    "secular",
    "theocracy (animism)",
    "theocracy (polytheism)",
    "theocracy (monotheism)",
    "hunter-gatherer",
    "agrarian",
    "industrial",
    "post-industrial",
    "transhuman",
    "hive mind",
    "nomadic city-state",
    "cybernetic society",
    "virtual society",
    "symbiotic society",
    "feudal (medieval europe inspired)",
    "democratic (ancient greece inspired)",
    "empire (roman empire inspired)",
    "shogunate (feudal japan inspired)",
    "guild system (medieval europe inspired)",
    "dystopian (1984 inspired)",
    "dystopian (the hunger games inspired)",
    "utopian (star trek inspired)",
    "utopian (utopia inspired)",
    "hive mind (ender's game inspired)",
    "hive mind (the borg inspired)",
    "spacefaring (star wars inspired)",
    "spacefaring (dune inspired)",
    "matriarchal theocracy",
    "nomadic technocracy",
    "hive mind barter system",
    "cybernetic republic",
    "virtual gift economy",
    "symbiotic feudal system",
    "egalitarian monarchy",
    "nomadic monarchy (constitutional)",
    "hunter-gatherer theocracy (animism)",
    "agrarian technocracy",
    "industrial republic (federal)",
    "post-industrial theocracy (polytheism)",
    "transhuman guild system",
    "nomadic caste system",
    "cybernetic extended family",
    "virtual nuclear family",
    "symbiotic resource-based economy",
    "egalitarian oligarchy",
    "nomadic dictatorship",
    "hunter-gatherer command economy",
    "agrarian sharing economy",
    "industrial capitalism (free market)",
    "post-industrial socialism (democratic socialism)",
    "transhuman meritocracy",
    "nomadic hive mind (resource-based)",
    "cybernetic theocracy (monotheism)",
    "virtual republic (unitary)",
    "symbiotic guild system (tech integration)",
    "matriarchal, agrarian republic",
    "nomadic, industrial technocracy",
    "hunter-gatherer, cybernetic theocracy",
    "post-industrial sharing economy with gerontocracy",
    "transhuman hive mind with advanced barter system",
    "virtual, symbiotic society with egalitarian governance"
]

character_roles = [
    "nomadic scholar", "warrior", "healer", "merchant", "artisan", "farmer",
    "explorer", "alchemist", "mystic", "diplomat", "inventor", "scribe",
    "hunter", "blacksmith", "weaver", "potter", "architect", "sculptor",
    "sailor", "caravan guide", "bard", "priest", "apothecary", "herbalist",
    "engineer", "cartographer", "astronomer", "scholar", "philosopher", "strategist",
    "assassin", "mercenary", "bodyguard", "gladiator", "shaman", "druid",
    "trader", "merchant-prince", "caravaneer", "peddler", "jeweler", "metalsmith",
    "woodcarver", "leatherworker", "glassblower", "textileartisan", "archer", "swordsman",
    "lancer", "shield-maiden", "warlock", "summoner", "elementalist", "necromancer",
    "ranger", "tracker", "survivalist", "guide", "trapper", "forager",
    "farmer", "shepherd", "vineyard-keeper", "fisherman", "miller", "baker",
    "brewer", "distiller", "cook", "vintner", "gardener", "florist",
    "architect", "mason", "carpenter", "stonemason", "engineer", "inventor",
    "scribe", "calligrapher", "historian", "librarian", "sage", "tutor",
    "diplomat", "ambassador", "spy", "informant", "negotiator", "aristocrat",
    "noble", "courtier", "advisor", "chancellor", "regent", "regent"
]

ethnicities = [
    "Aelvin", "Zyrex", "Ishari", "Kragnar", "Thalassian", "Darivian", "Amargyn",
    "Elorian", "Kordish", "Valyrian", "Shivaran", "Najiri", "Taldan", "Morianthi",
    "Kaelar", "Dazrin", "Quessiri", "Turux", "Shindari", "Elythian", "Zhanjia",
    "Hisari", "Valtaran", "Dashari", "Norvani", "Estrylian", "Gaeldrin", "Lyrithian",
    "Delkari", "Ishvari", "Kyranian", "Zoltani", "Shaerys", "Daranthian", "Fydorian",
    "Xander", "Navarri", "Solithar", "Valverian", "Menthari", "Destrian", "Myronian",
    "Karthian", "Dragonborn", "Elven", "Dwarven", "Halfling", "Gnomish", "Orc",
    "Goblin", "Troll", "Ogre", "Centaur", "Minotaur", "Harpy", "Satyr",
    "Naga", "Merfolk", "Triton", "Pixie", "Faerie", "Djinn", "Salamander",
    "Sylph", "Undine", "Gnome", "Goliath", "Firbolg", "Tabaxi", "Kenku",
    "Tiefling", "Aasimar", "Dragonborn", "Svirfneblin", "Duergar", "Githyanki", "Githzerai"
]


if core_concept_input:
    world_description = generate_world_seed(core_concept_input)

    st.subheader("World Description:")
    for category, description in world_description.items():
        st.write(f"{category.capitalize()}: {description}")

    # Generate cultural tapestry with random societal structure
    societal_structure = random.choice(societal_structures)
    cultural_descriptions = generate_cultural_tapestry(societal_structure, world_description)

    st.subheader("Cultural Tapestry:")
    for category, description in cultural_descriptions.items():
        st.write(f"{category.capitalize()}: {description}")

    # Generate character with random role and ethnicity
    character_role = random.choice(character_roles)
    ethnicity = random.choice(ethnicities)
    character_descriptions = generate_character(character_role, ethnicity)

    st.subheader("Character Description:")
    for category, description in character_descriptions.items():
        st.write(f"{category.capitalize()}: {description}")
