import json
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List

CONTACTS_FILE = "../contacts.json"

def load_contacts(filename=CONTACTS_FILE):
    with open(filename, "r") as f:
        return json.load(f)

contacts = load_contacts()

class Contact(BaseModel):
    id: int
    firstName: str
    lastName: str
    phoneNumber: str
    address: str
    age: int


class ContactInput(BaseModel):
    firstName: str
    lastName: str
    phoneNumber: str
    address: str
    age: int

app = FastAPI()

app.mount("/static", StaticFiles(directory="public", html=True), name="static")

@app.get("/")
def read_root():
   return FileResponse("public/index.html")

@app.get("/api/contacts", response_model=List[Contact])
def get_contacts():
    return JSONResponse(status_code=501, content={"error": "Not implemented"})

@app.post("/api/contacts")
def create_contact(new_contact: ContactInput):
    return JSONResponse(status_code=501, content={"error": "Not implemented"})

@app.delete("/api/contacts/{contact_id}")
def delete_contact(contact_id: int):
    return JSONResponse(status_code=501, content={"error": "Not implemented"})
