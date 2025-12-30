from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from typing import List, Dict, Optional


def get_database():
    try:
        client = MongoClient(
            "mongodb://localhost:27017/", serverSelectionTimeoutMS=5000
        )
        client.admin.command("ping")
        print("✓ Successfully connected to MongoDB!")

        db = client["contacts_data"]
        return db

    except ConnectionFailure as e:
        print(f"✗ Failed to connect to MongoDB: {e}")
        print("Make sure MongoDB is running on localhost:27017")
        return None


db = get_database()
contact_collection = db["contacts"] if db is not None else None


def create_contact(contact_data: dict) -> str:
    result = contact_collection.insert_one(contact_data)
    return result.inserted_id

def get_all_contacts() -> List[contact_collection]:
    result = contact_collection.find()
    if result is None:
        return []

def update_contact(id: str, contact_data: dict) -> bool:
    pass 
def delete_contact(id: str) -> str:
    pass