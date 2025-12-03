class Stats:
    """
    A simple class representing combat statistics for a monster or entity.
    """
    def __init__(self, atk: int, defense: int, pv: int):
        self.atk = atk
        self.defense = defense
        self.pv = pv

    def to_dict(self) -> dict:
        """
        Converts the stats object into a dictionary
        """
        return {
            "atk": self.atk,
            "defense": self.defense,
            "pv": self.pv
        }

    def take_damage(self, amount: int) -> int:
        """
        Apply incoming damage reduced by defense.
        Returns the final damage taken.
        """
        reduced_damage = max(amount - self.defense, 0)
        self.pv -= reduced_damage
        return reduced_damage

    def is_alive(self) -> bool:
        """Returns True if pv > 0."""
        return self.pv > 0

    def heal(self, amount: int):
        """Heals the entity."""
        self.pv += amount