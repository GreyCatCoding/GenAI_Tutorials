# GenAI_Tutorials
A simple tutorial of python and GenAi using VsCode.Lastly a flight booking application in accordance to agentic Ai with no external frameworks.  

INTRODUCTION TO GEMINI(introduction.py)
- Understand and generate text, images , audio , video and code

basic workflow
-take input prompt
-make an api request using python library for google gemino
- display the ai response in terminal
------------------------------------------
TEXT/ IMAGE GENERATION (textgeneration.py)

input > text or image
output > text

- system instructions 
- temperature 
- multimodal behaviour 
- streaming responses
------------------------------
chat conversation history (chatbot.py , advchatbot.py)
- user to agent
- saving chat session as chat history
--------------------
Structured text generation (structured.py)
- standard responses rather then random
- fetching from json or enum values
-----------------------
DOCUMENT READING (readdoc.py)
- understand pdf documents
- extract information from it which can be structured
- load pdf from  url or local files in computer
- small files under 20mb
- large files over 20mb
------------------------------------------
Agentic AI with only python and gemini (no external frameworks)

ticketbooking.py

What this project is
A terminal-based AI agent that simulates booking a flight from Singapore to Tokyo. Built entirely with Python and the Gemini API — no LangChain, no ADK, no external agent frameworks. The agent plans its own steps, executes each one, and reports structured results including a simulated ticket price.
