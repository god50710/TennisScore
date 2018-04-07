from unittest import TestCase

from Game import Game
from TennisScore import TennisScore


class TestTennisScore(TestCase):
    def test_love_all(self):
        self.assertEqual("Love All", TennisScore.tennis_judge(Game("Eric", "Maru", 0, 0)))

    def test_love_fifteen(self):
        self.assertEqual("Love Fifteen", TennisScore.tennis_judge(Game("Eric", "Maru", 0, 1)))

    def test_love_thirty(self):
        self.assertEqual("Love Thirty", TennisScore.tennis_judge(Game("Eric", "Maru", 0, 2)))

    def test_love_forty(self):
        self.assertEqual("Love Forty", TennisScore.tennis_judge(Game("Eric", "Maru", 0, 3)))

    def test_fifteen_love(self):
        self.assertEqual("Fifteen Love", TennisScore.tennis_judge(Game("Eric", "Maru", 1, 0)))

    def test_thirty_love(self):
        self.assertEqual("Thirty Love", TennisScore.tennis_judge(Game("Eric", "Maru", 2, 0)))

    def test_fifteen_all(self):
        self.assertEqual("Fifteen All", TennisScore.tennis_judge(Game("Eric", "Maru", 1, 1)))

    def test_thirty_all(self):
        self.assertEqual("Thirty All", TennisScore.tennis_judge(Game("Eric", "Maru", 2, 2)))

    def test_deuce_3_vs_3(self):
        self.assertEqual("Deuce", TennisScore.tennis_judge(Game("Eric", "Maru", 3, 3)))

    def test_deuce_4_vs_4(self):
        self.assertEqual( "Deuce", TennisScore.tennis_judge(Game("Eric", "Maru", 4, 4)))

    def test_first_player_adv(self):
        self.assertEqual("Eric Advance", TennisScore.tennis_judge(Game("Eric", "Maru", 4, 3)))

    def test_second_player_adv(self):
        self.assertEqual("Maru Advance", TennisScore.tennis_judge(Game("Eric", "Maru", 3, 4)))

    def test_second_player_win_with_5_point(self):
        self.assertEqual("Maru Win", TennisScore.tennis_judge(Game("Eric", "Maru", 3, 5)))

    def test_first_player_win_with_6_point(self):
        self.assertEqual("Eric Win",TennisScore.tennis_judge(Game("Eric", "Maru", 6, 4)))
