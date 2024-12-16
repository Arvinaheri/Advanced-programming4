class FootballPlayer:
    def __init__(self, name, age, team, position, goals, matches):
        self.name = name
        self.age = age
        self.team = team
        self.position = position
        self.goals = goals
        self.matches = matches
    def player_first_number(self):
        return('The player name: '+ self.name)    
    def player_age(self):
        return("the"+self.name + 's age is ' + str(self.age))

class Defender(FootballPlayer):
    pass

class Goalkeeper(FootballPlayer):
    pass

class Forward(FootballPlayer):
    pass

defender = Defender('Rozbe Cheshmi', 34, 'Esteghlal', 'defender', 19, 368)
goalkeeper = Goalkeeper('Seyyed Hossein Hosseini', 32, 'Esteghlal', 'goalkeeper', 1, 265)
forward = Forward('Arman Ramezani', 33, 'Esteghlal', 'forward', 32, 268)

print(defender.player_first_number())
print(defender.player_age())
print(goalkeeper.player_first_number())
print(goalkeeper.player_age())
print(forward.player_first_number())
print(forward.player_age())