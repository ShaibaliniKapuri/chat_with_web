import os
from groq import Groq
from langchain_groq import ChatGroq

def initialize_llm() -> ChatGroq:
    # Retrieve the API key from environment variables
    api_key = os.environ.get("GROQ_API_KEY")
    
    if not api_key:
        raise ValueError("GROQ_API_KEY environment variable is not set. Please set it before running the application.")
    
    
    # Initialize the LLM with the Groq client
    llm = ChatGroq(temperature=0.7, model_name="llama-3.1-8b-instant", groq_api_key=api_key)
    
    return llm

