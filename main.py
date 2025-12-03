from utils.database import connect_db
from utils.Monster import monsters
from utils.Hero import heroes
from utils.show import clear_screen, show_leaderboard , show_menu



def get_user_input(prompt: str, choices: list[str] = None) -> str:
    """
    Prompt the user with a message and validate their choice.

    Args:
        prompt (str): The message to display to the user.
        choices (list[str], optional): List of valid choices (as strings).

    Returns:
        str: The validated user choice.
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


def get_character() -> list:
    """
    Return a list of available characters.
    """
    return ["Hero1", "Hero2"]


def get_user_team() -> list:
    """
    """
    print("Team Selection...")
    available_characters = get_character()
    team = []
    
    while len(team) < 3:
        print("\n Character available :")
        for i, char in enumerate(available_characters, 1):
            print(f"{i}. {char}")
        
        choice = get_user_input("Choose a caracter with number", [str(i) for i in range(1, len(available_characters)+1)])
        team.append(available_characters[int(choice)-1])
        print(f"Current Team: {team}")
    
    return team


def start_game(username : str) -> None:
    team = get_user_team()
    print(f"{username}, your team is ready : {team}")






def main():
    username = get_player_name()
    print(f"Bienvenue sur le Jeu : {username}")

    while True:
        clear_screen()
        show_menu()

        choix = get_user_input("Choisissez une option", ["1", "2", "3"])
        
        if choix == "1":
            start_game(username)
        elif choix == "2":
            show_leaderboard()
            input("Appuyez sur Entrée pour revenir au menu principal.")
        elif choix == "3":
            print("Au revoir !")
            break
        
        clear_screen()


if __name__ == "__main__":
    main()
