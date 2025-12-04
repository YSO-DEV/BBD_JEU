from typing import List
import random

from utils.database import connect_db, get_values
from models.Entity import Entity
from utils.Show import clear_screen, show_leaderboard, show_menu

db = connect_db()


def get_user_input(prompt: str, choices: list = None) -> str:
    """
    Args:
        prompt (str): The message to display to the user.
        choices (list[str], optional): List of valid choices (as strings).
    """
    if choices is None or len(choices) == 0:
        return input(f"{prompt}: ")
    
    while True:
        user_input = input(f"{prompt} ({'/'.join(choices)}): ")
        if user_input in choices:
            return user_input
        else:
            print(f"Choix invalide. Veuillez choisir parmi {choices}.")


def get_player_name() -> str:
    """
    Ask the player for their name.
    """
    username = get_user_input("Entrez votre nom d'utilisateur")
    print(f"Bienvenue, {username} !")
    return username


def team_battle(hero_team: List, monster_team: List) -> list:
    """
    """
    def get_alive(entities):
        return [e for e in entities if e.is_alive()]

    def attack_phase(attackers, defenders):
        alive_defenders = get_alive(defenders)
        for attacker in get_alive(attackers):
            if not alive_defenders:
                break
            target = random.choice(alive_defenders)
            target.take_damage(attacker.atk)
            print(f"{attacker.name} attacks {target.name} for {attacker.atk} damage! ({target.pv} HP left)")
            alive_defenders = get_alive(defenders)

    if not get_alive(hero_team):
        return "monster_team", [e.name for e in get_alive(monster_team)]
    if not get_alive(monster_team):
        return "hero_team", [e.name for e in get_alive(hero_team)]

    round_counter = 1
    while get_alive(hero_team) and get_alive(monster_team):
        print(f"\n--- Round {round_counter} ---")
        attack_phase(hero_team, monster_team)
        if not get_alive(monster_team):
            return "hero_team", [e.name for e in get_alive(hero_team)]

        attack_phase(monster_team, hero_team)
        if not get_alive(hero_team):
            return "monster_team", [e.name for e in get_alive(monster_team)]

        round_counter += 1

    winner_team, survivors = ("hero_team", get_alive(hero_team)) if get_alive(hero_team) else ("monster_team", get_alive(monster_team))
    return winner_team, [e.name for e in survivors]

def get_all_heroes_from_db() -> List[dict]:
    """
    Fetch all heroes from MongoDB database.
    """
    heroes_collection = get_values("heroes")
    return list(heroes_collection.find())


def get_all_monsters_from_db() -> List[dict]:
    """
    Fetch all monsters from MongoDB database.
    """
    monsters_collection = get_values("monsters")
    return list(monsters_collection.find())


def choose_team_from_heroes() -> List:
    """
    Let the player choose 3 heroes from the database.
    Returns a list of Entity objects.
    """
    heroes = get_all_heroes_from_db()
    
    if not heroes:
        print("Error: No heroes found in database!")
        return []
    
    print("Available heroes:")
    
    for index, hero in enumerate(heroes, 1):
        name = hero.get("name", "Unknown")
        atk = hero.get("atk", 0)
        defense = hero.get("def", hero.get("defense", 0))
        pv = hero.get("hp", hero.get("pv", 0))
        print(f"{index}. {name} (atk={atk}, def={defense}, pv={pv})")
    
    selected_team = []
    
    while len(selected_team) < 3:
        choice = get_user_input("Choose hero number", [str(i) for i in range(1, len(heroes) + 1)])
        chosen_hero = heroes[int(choice) - 1]
        selected_team.append(Entity(chosen_hero))
        print("Current team:", [hero.name for hero in selected_team])
    
    return selected_team


def build_random_monster_team(n: int = 3) -> List:
    """
    Build a random team of n monsters from the database.
    Returns a list of Entity objects.
    """
    monsters = get_all_monsters_from_db()
    
    if not monsters:
        print("Error: No monsters found in database!")
        return []
    
    # Pick random monsters
    selected_count = min(n, len(monsters))
    picked_monsters = random.sample(monsters, k=selected_count)
    
    return [Entity(m) for m in picked_monsters]


def start_game(username: str, team_size: int = 3) -> None:
    """
    Starts a game with infinite waves until all heroes die.
    Heroes keep their HP between waves.
    """
    print(f"Team selection for {username}")
    team = choose_team_from_heroes()[:team_size]
    
    if not team:
        print("Cannot start game without heroes!")
        return

    wave = 1
    while team:
        print(f"\n--- Wave {wave} ---")
        enemies = build_random_monster_team(len(team))
    
        print("Monsters appearing:", [m.name for m in enemies])

        winner_team, survivors = team_battle(team, enemies)

        if winner_team == "hero_team":
            print(f"Heroes won wave {wave}!")
            team = [h for h in team if h.name in survivors]
            print("Surviving heroes:", [h.name for h in team])
        else:
            print(f"Monsters won wave {wave}! Heroes are defeated.")
            team = []
            break


        wave += 1

    print("\nAll heroes have fallen. Game over!")


def main():
    username = get_player_name()
    while True:
        clear_screen()
        show_menu()
        choix = get_user_input("Choose an option", ["1", "2", "3"])
        if choix == "1":
            start_game(username)
            input("Press Enter to continue...")
        elif choix == "2":
            show_leaderboard()
            input("Going back to the main menu.")
        elif choix == "3":
            print("Au revoir !")
            break


if __name__ == "__main__":
    main()