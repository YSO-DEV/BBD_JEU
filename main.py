from utils.database import connect_db
from utils.Monster import monsters
from utils.Hero import heroes
from utils.show import clear_screen , show_leaderboard



connect_db("test")

def get_user_input(choice:str) -> str:
    """
    Returns:
        int: _description_
    """
    # print(choice)
    user_input = input(str(choice))
    return user_input
    
def get_player_name() -> str:
    """
    Returns:
        str: _description_
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
    
        print( "this is a test  : ")

        clear_screen()
        input("this is a test")
        
    
main()