#The project is building an app with the purpose of organizing football games. It keeps track of the players that are in for a scheduled game.
#It also measures players performances during the game regarding three parameters: goals, assists and substitutions.


class Player:
    def __init__(self, name, position, availability=True):
        self.name = name
        self.position = position
        self.status = availability
        self.games_played = 0
        self.goals = 0
        self.assists = 0

    def __repr__(self):
        return "{name} plays {position} and is {availability}".format(name=self.name, position=self.position, availability=self.status)
    
    def score_goal(self):
        self.goals = self.goals + 1
        print("{name} has scored a goal. Wonderful !".format(name=self.namename))

    def make_assist(self):
        self.assists = self.assists + 1
        print("{name} has made an assist. Class.".format(name=self.name))



class Game:
    def __init__(self, date, time, location, duration=90, max_players=12):
        self.date = date
        self.time = time
        self.location = location
        self.duration = duration
        self.max_players = max_players
        self.counter = 0
        self.players = []

    def __repr__(self):
        return "Your game is taking place on {date} at {time} in {location}. The total number of players you set for this game is {max_players}. You can start now organizing it.".format(date=self.date, time=self.time, location = self.location, max_players=self.max_players)

    def available(self):
        availability = Player(self.status)
        if availability == True:
            print("Perfect, {name} has been added to the game".format(name=self.name))
        else:
            print("{name} is not available for this game. Please, select another player.".format(name=self.name))

    def add_player(self):
        self.counter = self.counter + 1
        self.players.append(Player(self.name))
        print("{name} has been successfully added to the game.".format(name=self.name))
        if self.counter == self.max_players: 
            print("Great news, you are now complete for the game. Enjoy!")
        elif self.counter < self.max_players:
            print("You still need {num_of_players_left} to be complete for the game.".format(num_of_players_left=self.max_players - self.counter))
        elif self.counter > self.max_players:
            print("You are actually {counter} players. You are in overcapacity of {overcapacity} of players. You can either play with subs or remove players if needed".format(counter = self.counter, overcapacity=self.counter - self.max_players))

    def remove_player(self):
        self.counter = self.counter - 1
        self.players.remove(Player(self.name))
        print("{name} has been successfully removed from the game. You still now need {num_of_players_left} to be full for the game.".format(name=self.name, num_of_players_left=self.max_players - self.counter))



#List of regular players using class Player

hicham = Player("Hicham Laraqui", "Attack / Central Back / Right Back")
ibat = Player("Soufiane Ibat", "Central Back")
hassib = Player("Hassib benchekroun", "Cnetral Back")
sentissi = Player("Youssef Sentissi", "Goalkeeper / Middlefielder")
belarbi = Player("Yassine Belarbi", "Attack")
ould = Player("Hamza Ould", "Attack")
wadem = Player("Adam Mouline", "Goalkeeper")
sami = Player("Sami Benzeakour", "Middlefielder")
hosni = Player("Mehdi Hosni", "Right Back")
messaoud = Player("Amine Messaoudi", "Central Back")
abed = Player("Abed Charif Chefchaouni", "None")
lantry = Player("Hassan Lantry", "Attack")


#Set up game with class Game

first_game = Game("Friday", "18:00", "Ain Attiq", 90, 6)
print(first_game)

first_game.add_player()