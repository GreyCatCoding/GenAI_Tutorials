from google import genai
import os

# 1. Hardcode your key just to test (Replace with your actual key from AI Studio)
API_KEY = "YOUR_API_KEY_HERE" 

try:
    print("Connecting to Google...")
    client = genai.Client(api_key=API_KEY)

    prompt = input("Enter your prompt: ")

    print("Sending to Gemini...")
    response = client.models.generate_content(  
        model='', # Specify the model
        contents=prompt
    )

    print("The response is:")
    print(response.text)

except Exception as e:
    print(f"FAILED! Error details: {e}")