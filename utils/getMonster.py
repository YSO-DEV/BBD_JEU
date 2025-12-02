from .database import connect_db

connect_db("monster")


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
