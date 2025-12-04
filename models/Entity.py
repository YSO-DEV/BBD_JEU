class Entity:
    """
    Small adapter for dicts or model instances.
    Normalized fields: name, atk, defense, pv
    """
    def __init__(self, src):
        if isinstance(src, dict):
            self.name = src.get("name") or src.get("Name")
            self.atk = int(src.get("atk", src.get("atk_value", 0)))
            self.defense = int(src.get("defense", src.get("def", 0)))
            self.pv = int(src.get("pv", src.get("hp", 0)))
        else:
            self.name = getattr(src, "name", "Unknown")
            self.atk = int(getattr(src, "atk", 0))
            self.defense = int(getattr(src, "defense", getattr(src, "def", 0)))
            self.pv = int(getattr(src, "pv", getattr(src, "hp", 0)))
        self.max_pv = max(self.pv, 1)

    def is_alive(self) -> bool:
        return self.pv > 0

    def take_damage(self, amount: int) -> int:
        dmg = max(amount - self.defense, 0)
        self.pv = max(self.pv - dmg, 0)
        return dmg

    def attack(self, other: "Entity") -> int:
        return other.take_damage(self.atk)
