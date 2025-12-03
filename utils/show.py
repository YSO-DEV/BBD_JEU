
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    

def show_leaderboard() -> None:
    """
    Returns a list of score instances.
    
    Returns:
        list[score]: List containing score objects
    """
    print( "Showing the Leaderboard")
    
    
def show_menu( ) -> None:
    """
    
    """
    print("\n=== Menu ===")
    print("1. Start the game")
    print("2. Show the leaderboard")
    print("3. Quit")
    
def show_score() -> None :
    """
    
    """
    print ("showing the score of the user")