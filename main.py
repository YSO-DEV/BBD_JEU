from utils.database import connect_db
from utils.Monster import monsters
from utils.Hero import heroes

connect_db("test")

def show_leaderboard() -> None:
    """
    Returns a list of score instances.
    
    Returns:
        list[score]: List containing score objects
    """
    print( "Showing the Leaderboard")



def get_user_input(choice:str) -> str:
    """
    Returns:
        int: _description_
    """
    # print(choice)
    user_input = input(str(choice))
    return user_input
    
def get_player_name():
    """
    
    """
    username = get_user_input("what is your name? ")
    print( username )
    return username


def get_character() -> list:
    """

    Returns:
        list: get the list of the availlable character
    """
    return list("hey", "test")
    
    
def get_user_team () -> list:
    """
    
    """
    print ( "getting the user team")
    
    return list("hey")
    


def main():
    
    username = get_player_name()
    
    print(f"Bienvenue sur le Jeu :  {username}")

    print("veuillez choisir votre equipe ")
    get_user_team()
    
    while True: 
        show_leaderboard()
        
        get_user_input("")
    
    
# main()