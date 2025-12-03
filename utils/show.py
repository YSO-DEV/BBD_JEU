
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