from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from typing import List, Dict, Optional
from bson import ObjectId

class Interactor:
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

    @staticmethod
    def create_contact(contact_data: dict) -> str:
        result = Interactor.contact_collection.insert_one(contact_data)
        return {
        "message": "contact created successfully",
        "id": str(result.inserted_id)
    }
    
    @staticmethod
    def get_all_contacts() -> List:
        result = list(Interactor.contact_collection.find())
        return result
    
    @staticmethod
    def update_contact(id: str, contact_data: dict) -> str:
        result = Interactor.contact_collection.update_one({"_id":ObjectId(id)},
                                                          {"$set":{"first_name":contact_data["first_name"],
                                                           "last_name":contact_data["last_name"],
                                                           "phone_number":contact_data["phone_number"]}})
        return {
        "message": "contact updated successfully",
        "id": str(result.upserted_id)
    }

    @staticmethod
    def delete_contact(id: str) -> str:
        result = Interactor.contact_collection.delete_one({"_id":ObjectId(id)})
        return {
        "message": "contact deleted successfully",
        "id": str(result.deleted_count)
    }