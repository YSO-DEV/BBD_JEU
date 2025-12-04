from utils.database import connect_db
import pymongo 

COLLECTION_NAME = "monsters"


def insert_monster(monster_data: dict) -> bool:
    """    
    Args:
        monster_data: Dictionary with keys: name, atk, defense (or def), pv (or hp)
    
    Returns:
        True if successful, raises ValueError if duplicate
    """
    db = connect_db()
    collection = db[COLLECTION_NAME]
    
    collection.create_index("name", unique=True)

    try:
        print(f"Trying to add {monster_data} to the database")
        collection.insert_one(monster_data)
        print("Monster inserted successfully")
        return True
        
    except pymongo.errors.DuplicateKeyError:
        raise ValueError("Duplicate key: monster with this name already exists")


def delete_monster(monster_name: str) -> bool:
    """
    
    Args:
        monster_name: Name of the monster to delete
    
    Returns:
        True if deleted, False if not found
    """
    db = connect_db()
    collection = db[COLLECTION_NAME]

    monster = collection.find_one({"name": monster_name})

    if monster is None:
        print(f"Monster '{monster_name}' not found in the database.")
        return False

    print(f"Deleting monster with _id: {monster['_id']}")

    result = collection.delete_one({"_id": monster["_id"]})

    if result.deleted_count > 0:
        print(f"Monster '{monster_name}' deleted successfully.")
        return True
    else:
        print("Failed to delete monster.")
        return False


def get_all_monsters() -> list:
    """
    
    Returns:
        List of monster documents
    """
    db = connect_db()
    collection = db[COLLECTION_NAME]
    
    return list(collection.find())


def get_monster_by_name(name: str) -> dict:
    """
    Get a specific monster by name.
    
    Args:
        name: Name of the monster
    
    Returns:
        Monster document or None if not found
    """
    db = connect_db()
    collection = db[COLLECTION_NAME]
    
    return collection.find_one({"name": name})


def get_monster_by_id(id: str) -> dict:
    """
    
    Args:
        id: MongoDB ObjectId as string
    
    Returns:
        Monster document or None if not found
    """
    from bson.objectid import ObjectId
    
    db = connect_db()
    collection = db[COLLECTION_NAME]
    
    try:
        return collection.find_one({"_id": ObjectId(id)})
    except:
        print(f"Invalid ID format: {id}")
        return None


def update_monster(name: str, updates: dict) -> bool:
    """

    Args:
        name: Name of the monster to update
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