from fastapi import FastAPI
import json
app = FastAPI()

def load_data():
    with open('patient.json','r') as f :
     data = json.load(f)

@app.get('/view')

def view():
   data = load_data()
   return data



@app.get("/")  
 
def home():
    return {"message": "Patient Managment System"}

@app.get("/about")

def about():
    return{'message':'About the Hospital Patient '}