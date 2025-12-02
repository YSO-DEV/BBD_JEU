class Team:
    def __init__(self, name:str):
        self.name = name
        
    def team(self):
        print(self.name)
        
        
foo = Team("avenger")
foo.team()