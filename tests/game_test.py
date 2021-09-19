import unittest

from models.game import Game
from models.player import Player
from controllers import controller

class TestGame(unittest.TestCase):

    # from models.game import Game

    def setUp(self):
        self.game1 = Game("Iain", "Iain2", "rock", "paper" )
        # self.game2 = Game("Matt Hardy", "scissors")
    

    # # def test_game_has_player(self):
    # #     self.assertEqual("Jeff Hardy", self.game1.player)

    # # def test_game_has_player_choice(self):
    # #     self.assertEqual("rock", self.game1.player_choice)


    # # def test_game_has_winner(self):
    # #     self.assertEqual("YOU WIN!", Game.play_game(self))

    # def test_game_is_draw(self):
    #     self.assertEqual("IT'S A TIE", Game.play_game(self))
    
    def test_play_game(self):
        self.assertEqual('The winner is player 1', Game.player1_name, Game.play_game(self))