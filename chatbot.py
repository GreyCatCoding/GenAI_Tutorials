from google import genai
from google.genai import types


client = genai.Client()

print("Chatbot is running\ntype endchat to exit")
chathistory= []#initialize chat history list #store the conversation history for chatbot  reference
userinput = input("Ask me something : ")

while userinput != "endchat":
    chathistory.append(userinput)#append user input to chat history
    systemoutput = client.models.generate_content(
        model='gemini-2.5-flash-lite',
        #contents=userinput,#single input
        contents=chathistory,#multiple inputs from chat history #contents that the model will use to generate a response
        config=types.GenerateContentConfig(
            system_instruction="answer in one line with a maximum of 15 words,be more human",
            
        )
    )
    chathistory.append(systemoutput.text)#append system output to chat history
    print("ryobot says: " + systemoutput.text)
    userinput = input("Ask me something : ")



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