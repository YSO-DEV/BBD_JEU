from pymongo import MongoClient

def init_database(uri="mongodb://localhost:27017/", db_name="PythonGame"):
    """
    Initialize MongoDB database with default heroes and monsters.
    """
    client = MongoClient(uri)
    db = client[db_name]

    # Collections
    heroes_col = db["heroes"]
    monsters_col = db["monsters"]

    heroes_col.delete_many({})
    monsters_col.delete_many({})

    monsters = {
        "gobelin": {"name": "Gobelin", "atk": 10, "def": 5, "hp": 50},
        "orc": {"name": "Orc", "atk": 20, "def": 8, "hp": 120},
        "dragon": {"name": "Dragon", "atk": 35, "def": 20, "hp": 300},
        "zombie": {"name": "Zombie", "atk": 12, "def": 6, "hp": 70},
        "troll": {"name": "Troll", "atk": 25, "def": 15, "hp": 200},
        "spectre": {"name": "Spectre", "atk": 18, "def": 10, "hp": 100},
        "golem": {"name": "Golem", "atk": 30, "def": 25, "hp": 250},
        "vampire": {"name": "Vampire", "atk": 22, "def": 12, "hp": 150},
        "loup_garou": {"name": "Loup-garou", "atk": 28, "def": 18, "hp": 180},
        "squelette": {"name": "Squelette", "atk": 15, "def": 7, "hp": 90}
    }

    # Default heroes
    heroes = {
        "guerrier": {"name": "Guerrier", "atk": 15, "def": 10, "hp": 100},
        "mage": {"name": "Mage", "atk": 20, "def": 5, "hp": 80},
        "archer": {"name": "Archer", "atk": 18, "def": 7, "hp": 90},
        "voleur": {"name": "Voleur", "atk": 22, "def": 8, "hp": 85},
        "paladin": {"name": "Paladin", "atk": 14, "def": 12, "hp": 110},
        "sorcier": {"name": "Sorcier", "atk": 25, "def": 3, "hp": 70},
        "chevalier": {"name": "Chevalier", "atk": 17, "def": 15, "hp": 120},
        "moine": {"name": "Moine", "atk": 19, "def": 9, "hp": 95},
        "berserker": {"name": "Berserker", "atk": 23, "def": 6, "hp": 105},
        "chasseur": {"name": "Chasseur", "atk": 16, "def": 11, "hp": 100}
    }

    # Insert into collections
    monsters_col.insert_many([v for v in monsters.values()])
    heroes_col.insert_many([v for v in heroes.values()])

    print(f"Database '{db_name}' initialized with {len(monsters)} monsters and {len(heroes)} heroes.")


# Example usage
if __name__ == "__main__":
    init_database()
