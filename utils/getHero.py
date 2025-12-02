from database import connect_db
import pymongo


COLLECTION_NAME = "heroes"

class Hero:
    def __init__(self, name: str, atk: int, defense: int, pv: int):
        self.name = name
        self.atk = atk
        self.defense = defense
        self.pv = pv
    
    @classmethod
    def create_all_hero(cls):
        """
        Returns a dictionary of all predefined heroes.
        """
    
        
        return {
            "guerrier": cls("Guerrier", 15, 10, 100),
            "mage": cls("Mage", 20, 5, 80),
            "archer": cls("Archer", 18, 7, 90),
            "voleur": cls("Voleur", 22, 8, 85),
            "paladin": cls("Paladin", 14, 12, 110),
            "sorcier": cls("Sorcier", 25, 3, 70),
            "chevalier": cls("Chevalier", 17, 15, 120),
            "moine": cls("Moine", 19, 9, 95),
            "berserker": cls("Berserker", 23, 6, 105),
            "chasseur": cls("Chasseur", 16, 11, 100),
        }
        
heroes = Hero.create_all_hero()


def insert_hero():
    db = connect_db()
    collection = db[COLLECTION_NAME]
    
    collection.create_index("name", unique=True)

    hero_data = {
        "name": "guerrier",
        "atk": 12,
        "defense": 28,
        "pv": 120
        }
    try:
        print(f"Trying adding {hero_data} in the database {collection}")
        collection.insert_one(hero_data)
        print("Hero inserted successfully")
        
    except pymongo.errors.DuplicateKeyError:
        raise ValueError("Duplicate key: hero with this name already exists")
    


def delete_hero():
    db = connect_db()
    collection = db[COLLECTION_NAME]

    hero = collection.find_one({"name": "guerrier"})

    if hero is None:
        print("Hero 'guerrier' not found in the database.")
        return

    print(f"Deleting hero with _id: {hero['_id']}")

    result = collection.delete_one({"_id": hero["_id"]})

    if result.deleted_count > 0:
        print("Hero 'guerrier' deleted successfully.")
    else:
        print("Failed to delete hero.")



def get_all_hero ( ) -> list:
    db = connect_db()
    collection = db[COLLECTION_NAME]
    
    print("All the heroes : ")
    for elements in collection.find():
        print(elements ["_id"])
    
    
    return collection.find()


def get_hero_by_id( id:str ) -> dict:
    db = connect_db()
    collection = db[COLLECTION_NAME]
    
    print(f"The Element from ID : {collection}")
    collection.find( { "_id" : id })
    
    print ( collection.find({ "_id":id}))
    
    
    
get_hero_by_id( "692f03075a6aca07076227f4" )
get_all_hero()


# delete_hero()
# insert_hero()

