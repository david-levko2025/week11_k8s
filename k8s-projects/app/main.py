from fastapi import FastAPI,HTTPException
from typing import Annotated,List
from data_interactor import Interactor
import uvicorn
from contact import Contact


app = FastAPI()


@app.get("/contacts")
def get_all_collection() -> list[Contact]:
    all_collection = Interactor.get_all_contacts()
    return all_collection

@app.post("/contacts")
def create_new_contact(contact: Contact) -> dict:
    new = contact.model_dump()
    new_contact = Interactor.create_contact(new)
    return new_contact

@app.put("/contacts/{id}")
def update_existing_contact(id,contact:Contact) -> dict:
    update_contact_ = Interactor.update_contact(id, contact)
    return update_contact_
    
@app.delete("/contacts/{id}")
def delete_contact(id) -> dict:
    delete_info = Interactor.delete_contact(id)
    return delete_info



if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)