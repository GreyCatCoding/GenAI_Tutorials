from google import genai
from google.genai import types
from pydantic import BaseModel#structured output
from typing import Optional# for optional fields in the structured output
import json# for parsing json data 

# a def is used when we want to define a function that perfoerms a specific task
# a class is used when we want to create a blueprint for an object that can have attributes and methods

#Sequence of steps to achieve the goal
# run -> plan steps -> execute steps -> completed steps

# RESPONSE STRUCTURES 
class PlanStep(BaseModel):# defining a structured schema for the steps in the plan
    step_name: str
class Executetask(BaseModel):# defining a structured schema for the execution of a task
    task_name: str
    action_taken: str
    results_summary: str
    simulated_data: Optional[str] = None # an optional field to represent any simulated data if required, as not all tasks may require simulation

# USE OF LLM MODEL
def CallModel(prompt,schema):# defining a function to call the model with a given prompt and schema
    response = chat.send_message(prompt, config=types.GenerateContentConfig(# defining the configuration for the content generation
            response_schema=schema,# defining the schema for the response, which is a list of PlanStep objects such as step_name
            response_mime_type="application/json",# specifying that we want the response in JSON format
            system_instruction="answer in less than 100 words"# providing a system instruction to the model to answer in less than 100 words
    
    ) ) 
    return response.text
    
#--------------------------------------------------------------------------------------------------------

# CREATE PLAN/AGENT # MAIN
def run_agent(): # defining the main function to run the agent
    steps = plan_goal()# calling the plan_goal function to get the steps required to achieve the goal
    for step in steps:
        execute_step(step)
    print("\n completed steps \n")

def execute_step(step): # defining a function to execute a given step
    print("-------------------------------------------------------")
    actionprompt = f"execute the following step: {step}. Describe what you did and summarise the results.Simulate the task if required" # defining the prompt to ask the agent to execute the given step
    result = CallModel(actionprompt, Executetask) # calling the CallModel function with the actionprompt and the schema for the response
    result = json.loads(result) # parsing the response from the model as JSON data to a dictionary as we cannot extract data from a string response

    print(f"Task Name: {result['task_name']}") # printing the task name from the result
    print(f"Action Taken: {result['action_taken']}") # printing the action taken
    print(f"Results Summary: {result['results_summary']}") # printing the results summary

    if result['simulated_data']: # checking if there is any simulated data in the result
        print(f"Simulated Data: {result['simulated_data']}") # printing the simulated data if it exists
    print("-------------------------------------------------------")

def plan_goal():
    plan_prompt = "break the goal into clear , numbered steps"# defining the prompt to ask the agent to break the goal into clear, numbered steps
    plans = CallModel(plan_prompt,list[PlanStep]) # calling the CallModel function with the plan_prompt and the schema for the response,
    # list of string steps
    plans = json.loads(plans) # parsing the response from the model as JSON data to a diqtionary as we cannot extract data from a string response
    steps = [plan['step_name'].strip() for plan in plans if plan['step_name'].strip()] # extracting the step names from the response and stripping any leading or trailing whitespace, also checking if the step name is not empty
    return steps


if __name__ == "__main__":
    client = genai.Client()
    model = "gemini-2.5-flash-lite" 

    chat = client.chats.create(model=model) # creating a chat instance using the specified model
    goal="Book a ticket from Singapore to Japan Tokyo"# defining the goal for the agent 
    print(f"Goal: {goal}")# printing the goal to the console

    #modifying the goal to provide more context and instructions to the agent
    modified_goal = f"""you are virtual agent expert in booking flight tickets, your task is to {goal} 
    Acknowledge the goal for now , i will then ask you to create a plan to execute
    """ 
    chat.send_message(modified_goal) # sending the modified goal to the agent through the chat instance
    run_agent() # calling the run_agent function to start the agent's execution





