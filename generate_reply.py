from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

def gen_reply(chat: str):
    prompt = f"""
    You are my personal assistant of Rinshi. 
    Here is my chat: {chat} 
    Reply like how I would normally reply to messages. 
    Understand the tone of messages. 
    Keep the reply short.
    The language in chat include english, malayalam and manglish
    """

    # Initialize the model
    model = genai.GenerativeModel("gemini-1.5-flash")

    # Generate a reply
    response = model.generate_content(prompt)

    return response.text
