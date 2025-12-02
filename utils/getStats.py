from .database import connect_db


def get_damage(user_id: str):
    connect_db("test")
    print(f"getting the {user_id} damages")


get_damage( "my user id ")

