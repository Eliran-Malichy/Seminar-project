from Player import Player
from datetime import datetime
from time import time


class GameInfo:
    def __init__(self, player_id, player_name):
        """
        init Game_info
        :param player_id: player id
        :param player_name: player name
        """
        self.player_id = player_id
        self.player_name = player_name
        self.time_created = time()
        self.num_rounds = 0
        self.winner = None

    def increase_num_rounds(self):
        """
        increase number of rounds played in a game
        """
        self.num_rounds = self.num_rounds + 1

    def get_player_id(self):
        """
        returns player's id
        """
        return self.player_id

    def get_player_name(self):
        """
        returns player's name
        """
        return self.player_name

    def start_new_game(self):
        """
        reset all values
        """
        self.winner = None
        self.num_rounds = 0
        self.time_created = time()