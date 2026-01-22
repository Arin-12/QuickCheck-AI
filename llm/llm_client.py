import os
from google import genai

# Load API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise RuntimeError("GEMINI_API_KEY not set")

# Initialize client
client = genai.Client(api_key=GEMINI_API_KEY)

def call_llm(prompt: str) -> str:
    response = client.models.generate_content(
        model="models/gemini-2.5-flash",  #✅ FULL MODEL PATH
        contents=prompt
    )
    return response.text
