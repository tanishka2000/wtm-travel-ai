from fastapi import FastAPI
import google.generativeai as gemini
import os

os.environ['GOOGLE_API_KEY'] = "your-api-key-here"
gemini.configure(api_key = os.environ['GOOGLE_API_KEY'])

model = gemini.GenerativeModel('gemini-1.5-flash')

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/")
def generateOutput(userInput):
    responseData = model.generate_content(userInput)
    return responseData
