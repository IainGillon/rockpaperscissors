import unittest


from models.player import Player


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player1 = Player("Jeff Hardy", "rock")
        self.player2 = Player("Matt Hardy", "paper")

    def test_player_has_name(self):
        self.assertEqual("Jeff Hardy", self.player1.name)
    
    def test_player_has_choice(self):
        self.assertEqual("paper", self.player2.choice)
