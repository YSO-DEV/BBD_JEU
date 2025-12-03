
from .database import connect_db
import pymongo 

COLLECTION_NAME = "monsters"

class Monster:
    def __init__(self, name: str, atk: int, def_: int, pv: int):
        self.name = name
        self.atk = atk
        self.def_ = def_
        self.pv = pv
    
    @classmethod
    def create_all_monster(cls):
        """
        Returns a dictionary of all predefined monsters.
        """
        
        
        return {
            "gobelin": cls("Gobelin", 10, 5, 50),
            "orc": cls("Orc", 20, 8, 120),
            "dragon": cls("Dragon", 35, 20, 300),
            "zombie": cls("Zombie", 12, 6, 70),
            "troll": cls("Troll", 25, 15, 200),
            "spectre": cls("Spectre", 18, 10, 100),
            "golem": cls("Golem", 30, 25, 250),
            "vampire": cls("Vampire", 22, 12, 150),
            "loup_garou": cls("Loup-garou", 28, 18, 180),
            "squelette": cls("Squelette", 15, 7, 90),
        }


monsters = Monster.create_all_monster()


def insert_monster() -> bool:
    db = connect_db()
    collection = db[COLLECTION_NAME]
    
    collection.create_index("name", unique=True)

    monster_data = {
        "name": "guerrier",
        "atk": 12,
        "defense": 28,
        "pv": 120
        }
    try:
        print(f"Trying adding {monster_data} in the database {collection}")
        collection.insert_one(monster_data)
        print("monster inserted successfully")
        return True
        
    except pymongo.errors.DuplicateKeyError:
        raise ValueError("Duplicate key: monster with this name already exists")
    


def delete_monster() -> bool :
    db = connect_db()
    collection = db[COLLECTION_NAME]

    monster = collection.find_one({"name": "guerrier"})

    if monster is None:
        print("monster 'guerrier' not found in the database.")
        return False

    print(f"Deleting monster with _id: {monster['_id']}")

    result = collection.delete_one({"_id": monster["_id"]})

    if result.deleted_count > 0:
        print("monster 'guerrier' deleted successfully.")
    else:
        print("Failed to delete monster.")
        
    return True



def get_all_monster() -> list:
    db = connect_db()
    collection = db[COLLECTION_NAME]
    
    print("All the monsters : ")
    for elements in collection.find():
        print(elements ["_id"])
    
    
    return collection.find()


def get_monster_by_id( id:str ) -> dict:
    db = connect_db()
    collection = db[COLLECTION_NAME]
    
    print(f"The Element from ID : {collection}")
    collection.find( { "_id" : id })
    
    print ( collection.find({ "_id":id}))
    