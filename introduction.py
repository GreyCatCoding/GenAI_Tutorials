from google import genai

# Only run this block for Gemini Developer API
client = genai.Client()

prompt = input("Enter your prompt: ") # Get user input for the prompt

response = client.models.generate_content( # Use the Gemini model to generate content
    model='gemini-2.0-flash', # Specify the model
    contents=prompt# Provide the user input as content
)

print("The response is :")
print(response.text)