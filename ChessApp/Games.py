class GameDict:
    def __init__(self):
        self.games = {}

    def add_game(self, gamename, game):
        self.games.update({str(gamename): game})


gameDict = GameDict()

