from google import genai
from pydantic import BaseModel # for structured output ,
#  why? because it allows us to define a structured schema for the output,
# making it easier to parse and use the generated content in a more organized way.
import enum 

class Grade(enum.Enum): # defining an enum for the rating of the burger recipe
    A_PLUS = "A+"
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    F = "F"


#basemodel is a class from the pydantic library that allows us to define a structured schema for our data models.
# It provides features such as data validation, serialization, and parsing, making it easier to work with structured data in our applications. 
# By inheriting from BaseModel, we can define our own data models with specific fields and types, and pydantic will handle the validation and parsing of the data for us.


class BurgerRecipe(BaseModel): # defining a structured schema for the burger recipe
    recipename: str# string to represent the name of the burger recipe
    ingredients: list[str]# list of strings to represent the ingredients
    instructions: str
    rating: Grade # using the Grade enum to represent the rating of the burger recipe

client = genai.Client()

prompt = "list a few popular burger recipes with their ingredients and cooking instructions."

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents =  prompt,
    config = {
        "response_mime_type": "application/json", # specify that we want the response in JSON format
        "response_schema": list[BurgerRecipe],#a schema is used to define the structure of the data that we expect to receive in the response, in this case, we are expecting a list of BurgerRecipe objects. By specifying the response schema, we can ensure that the generated content adheres to a specific format and can be easily parsed and used in our application.
        # specify the schema for the response, which is a list of BurgerRecipe objects such as recipename, ingredients, instructions, and rating


    } # parsing json data as compared to text data is more structured and easier to work with
)

print(response.text)