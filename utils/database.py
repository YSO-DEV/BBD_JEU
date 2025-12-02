from pymongo import MongoClient
from dotenv import load_dotenv
import os


load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))


def connect_db():
    db = client["PythonGame"]
    print("Connected to database: PythonGame")
    return db


def get_values(collection_name: str):
    db = client["PythonGame"]
    collection = db[collection_name]
    print("All the collection:", collection_name)
    return collection


def show_all_values(collection_name: str):
    """
    Show all documents from the collection
    """
    collection = get_values(collection_name)
    
    print(f"\n=== All documents in {collection_name} ===")
    for element in collection.find():
        print(element)
    print("=" * 50)





# get_values( "PythonGame" , "heroes")
# show_all_values("PythonGame", "heroes")


