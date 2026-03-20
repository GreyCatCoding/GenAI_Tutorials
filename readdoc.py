from google import genai
from google.genai import types
import httpx# for making HTTP requests to fetch the content of the document from the provided URL
import pathlib # for working with file 
import io # for handling input and output operations, such as reading the content of the PDF document as bytes
client = genai.Client()

#FETCH DATA FROM URL
#doc_url = "" # URL of the document to be summarized
#doc_data = httpx.get(doc_url).content # fetching the content of the document from the provided URL using httpx library 

#FETCH DATA FROM LOCAL FILE PDF
filepath = pathlib.Path('pdf/Louis_Vuitton.pdf') # specifying the file path of the PDF document to be summarized
doc_data = filepath.read_bytes() # reading the content of the PDF document as bytes using pathlib library
prompt = "Summarize the document"# prompt to instruct the model to summarize the content of the document

pdf = types.Part.from_bytes(# creating a Part object from the bytes of the PDF document
    data = doc_data,
    mime_type="application/pdf"# specifying the MIME type of the document as PDF
)

#FETCH LONG CONTEXT PDF FROM URL
#long_context_pdf_path =""# specifying the file path of the PDF document with long context to be summarized
#doc_data = io.BytesIO(httpx.get(long_context_pdf_path).content) # fetching the content of the document from the provided URL using httpx library and reading it as bytes using io library

pdf = client.files.upload(# uploading the PDF document to the model using the client.files.upload method
    file=doc_data,
    config={
    "mime_type": "application/pdf" # specifying the MIME type of the document as PDF
    }
)

response = client.models.generate_content(
    model='gemini-2.5-flash',   
    contents = [pdf,prompt],
    config =types.GenerateContentConfig(
        system_instruction="answer in around 200 characters" # system instruction to specify the desired length of the summary
    )
)

print(response.text)