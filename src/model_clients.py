
# Standard-library imports
import os

# Third party imports
from openai import OpenAI
from dotenv import load_dotenv

# Load API credentials from the .env file into environment variables
load_dotenv()

def get_gemini_client():

    """ Initializes the OpenAI-compatible client using GEMINI API Key """
    gemini_client = OpenAI (  
        api_key=os.getenv("GEMINI_API_KEY"),     
        base_url="https://generativelanguage.googleapis.com/v1beta"   
    )
    return gemini_client

def get_groq_client():
    """ Initializes the OpenAI-compatible client using GROQ API Key """
    groq_client = OpenAI (  
        api_key=os.getenv("GROQ_API_KEY"),     
        base_url="https://api.groq.com/openai/v1"   
    )
    return groq_client