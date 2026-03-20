from google import genai
from google.genai import types# Importing necessary modules from the Google GenAI library to interact with the Gemini model and handle content generation tasks.
from PIL import Image # Importing the Python Imaging Library (PIL) to handle image processing tasks, such as opening and manipulating images.

# Only run this block for Gemini Developer API
client = genai.Client()

#prompt = input("Enter your prompt: ") # Get user input for the prompt
image = Image.open("images/image1.jpg") # Open an image file using PIL

response = client.models.generate_content_stream( # Use the Gemini model to generate content
    model='gemini-2.0-flash', # Specify the model
    #contents=prompt,# Provide the user input as content
    contents=[image,"Tell me about this image"], # Provide the image and a prompt asking for a description of the image
    config = types.GenerateContentConfig(# Optional configurations for content generation
    system_instruction="Responses should be in less than 20 words, be hilarious",# System instruction to guide the model's response
    temperature=2  
    # Set temperature to control randomness/creativity, # 0-2
    # lower values = less creativity / faster response , higher value = more creavity / slower response 
    )

)

for chunk in response:
    print(chunk.text, end='---\n---') # Print each chunk of the response as it is received
        

#print("The response is :")
#print(response.text)

#generate_content_stream #- Streams the response as it's being generated, allowing for real-time output.
#generate_content #- Waits for the full response before returning it.