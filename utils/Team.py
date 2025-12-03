class Teams:
    """
    Represents a team made of multiple Monster objects.
    """
    def __init__(self, name: str):
        self.name = name
        self.members: list = []  

    def add_monster(self, monster):
        """
        Adds a Monster to the team.
        """
        self.members.append(monster)

    def remove_monster(self, name: str) -> bool:
        """
        Removes a monster by name. Returns True if removed, False if not found.
        """
        for m in self.members:
            if m.name.lower() == name.lower():
                self.members.remove(m)
                return True
        return False

    def get_member(self, name: str):
        """
        Returns a monster by name, or None.
        """
        for m in self.members:
            if m.name.lower() == name.lower():
                return m
        return None

    def is_team_alive(self) -> bool:
        """
        Returns True if at least one monster is still alive.
        """
        return any(m.stats.is_alive() for m in self.members)

    def total_stats(self) -> dict:
        """
        Returns combined team statistics.
        """
        atk = sum(m.stats.atk for m in self.members)
        defense = sum(m.stats.defense for m in self.members)
        pv = sum(m.stats.pv for m in self.members)

        return {
            "total_atk": atk,
            "total_defense": defense,
            "total_pv": pv
        }
