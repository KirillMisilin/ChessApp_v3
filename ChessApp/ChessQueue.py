from .Game import Game
from datetime import datetime


class ChessQueue:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def can_find_game(self):
        if len(self.players) > 0:
            return True
        return False

    def create_game_name(self, player):
        current_datetime = datetime.now()
        game_name = "game_" + self.players[0] + "_vs_" + player + "_" +\
                    str(current_datetime.year) + str(current_datetime.day) +\
                    str(current_datetime.second) + str(current_datetime.microsecond)
        return game_name

    def create_game(self, player):
        if self.can_find_game():
            game1 = Game(self.players[0], player)
            # self.players.pop(1)
            self.players.pop(0)
            return game1
        else:
            return None


chessQueue = ChessQueue()
