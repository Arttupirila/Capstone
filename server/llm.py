import os 
import requests
from dotenv import load_dotenv
#uvicorn main:app --reload
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

def generate_response(user_prompt: str) -> str:
    system_prompt = (
        "You are a recipe generator. "
        "Give a recipe based on the ingredients provided."
        "Estimate the cooking time and difficulty level as well. "
        "If the ingredients are not sufficient to create a recipe, don't make up additional ingredients. Instead, respond with a message indicating that the recipe cannot be generated due to insufficient ingredients."
        "Format the response as follows:\n"
        "Recipe Name: <name>\n"
        "Ingredients:\n- <ingredient 1>\n- <ingredient 2>\n...\n"
        "Instructions:\n1. <step 1>\n2. <step 2>\n..."
        "\n"
        "Estimated Cooking Time: <time>\n"
        "Difficulty Level: <level>"
         )

    full_prompt = f"{system_prompt}\n\nUser: {user_prompt}"

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:generateContent?key={API_KEY}"

    data = {
        "contents": [{"parts": [{"text": full_prompt}]}]
    }

    try:
        res = requests.post(url, json=data)
        res.raise_for_status()
        return res.json()["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        return f"Error: {str(e)}"
    
