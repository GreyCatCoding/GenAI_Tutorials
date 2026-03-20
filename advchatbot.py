from google import genai
from google.genai import types


client = genai.Client()
chat = client.chats.create(model="gemini-2.5-flash",
                           config=types.GenerateContentConfig(
                                 system_instruction="answer in one line with a maximum of 20 words,be more human"
                           ))#initialize chat session with chat history management


print("Chatbot is running\ntype endchat to exit")
userinput = input("Ask me something : ")
while userinput != "endchat":
    response = chat.send_message(userinput)
    print("Ryobot:" + response.text)
    userinput = input("Ask me something : ")

print("-----------------------------------------------------------------------------")
for message in chat.get_history():#iterate through chat history
    print(f"role : {message.role}")  # Accessing the role of the message
    print(message.parts[0].text)  # Accessing the text content of the message

#def get_gemini_response(user_input):
    #response = client.models.generate_content(
      #  model='gemini-2.0-flash',
       # contents=[user_input],
       # config=genai.types.GenerateContentConfig(
       #     temperature=1.5,
        #    max_output_tokens=500
     #   )
  #  )
   # return response.text