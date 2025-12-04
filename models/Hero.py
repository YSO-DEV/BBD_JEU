from utils.database import connect_db
import pymongo

COLLECTION_NAME = "heroes"


def insert_hero(hero_data: dict) -> bool:
    """
    
    Args:
        hero_data: Dictionary with keys: name, atk, defense (or def), pv (or hp)
    
    Returns:
        True if successful, raises ValueError if duplicate
    """
    db = connect_db()
    collection = db[COLLECTION_NAME]
    
    collection.create_index("name", unique=True)

    try:
        print(f"Trying to add {hero_data} to the database")
        collection.insert_one(hero_data)
        print("Hero inserted successfully")
        return True
        
    except pymongo.errors.DuplicateKeyError:
        raise ValueError("Duplicate key: hero with this name already exists")


def delete_hero(hero_name: str) -> bool:
    """    
    Args:
        hero_name: Name of the hero to delete
    
    Returns:
        True if deleted, False if not found
    """
    db = connect_db()
    collection = db[COLLECTION_NAME]

    hero = collection.find_one({"name": hero_name})

    if hero is None:
        print(f"Hero '{hero_name}' not found in the database.")
        return False

    print(f"Deleting hero with _id: {hero['_id']}")

    result = collection.delete_one({"_id": hero["_id"]})

    if result.deleted_count > 0:
        print(f"Hero '{hero_name}' deleted successfully.")
        return True
    else:
        print("Failed to delete hero.")
        return False


def get_all_heroes() -> list:
    """
    Get all heroes from the database.
    
    Returns:
        List of hero documents
    """
    db = connect_db()
    collection = db[COLLECTION_NAME]
    
    return list(collection.find())


def get_hero_by_name(name: str) -> dict:
    """
    Get a specific hero by name.
    
    Args:
        name: Name of the hero
    
    Returns:
        Hero document or None if not found
    """
    db = connect_db()
    collection = db[COLLECTION_NAME]
    
    return collection.find_one({"name": name})


def get_hero_by_id(id: str) -> dict:
    """
    Get a specific hero by MongoDB _id.
    
    Args:
        id: MongoDB ObjectId as string
    
    Returns:
        Hero document or None if not found
    """
    from bson.objectid import ObjectId
    
    db = connect_db()
    collection = db[COLLECTION_NAME]
    
    try:
        return collection.find_one({"_id": ObjectId(id)})
    except:
        print(f"Invalid ID format: {id}")
        return None


def update_hero(name: str, updates: dict) -> bool:
    """
    Update a hero's attributes.
    
    Args:
        name: Name of the hero to update
        updates: Dictionary of fields to update
    
    Returns:
        True if updated, False if not found
    """
    db = connect_db()
    collection = db[COLLECTION_NAME]
    
    result = collection.update_one(
        {"name": name},
        {"$set": updates}
    )
    
    return result.modified_count > 0