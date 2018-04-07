from unittest import TestCase
from TennisScore import TennisScore


class TestTennisScore(TestCase):
    def test_love_all(self):
        self.assertEqual(TennisScore.tennis_judge("Eric", "Maru", 0, 0), "Love All")

    def test_love_fifteen(self):
        self.assertEqual(TennisScore.tennis_judge("Eric", "Maru", 0, 1), "Love Fifteen")

    def test_love_thirty(self):
        self.assertEqual(TennisScore.tennis_judge("Eric", "Maru", 0, 2), "Love Thirty")

    def test_love_forty(self):
        self.assertEqual(TennisScore.tennis_judge("Eric", "Maru", 0, 3), "Love Forty")

    def test_fifteen_love(self):
        self.assertEqual(TennisScore.tennis_judge("Eric", "Maru", 1, 0), "Fifteen Love")

    def test_thirty_love(self):
        self.assertEqual(TennisScore.tennis_judge("Eric", "Maru", 2, 0), "Thirty Love")

    def test_fifteen_all(self):
        self.assertEqual(TennisScore.tennis_judge("Eric", "Maru", 1, 1), "Fifteen All")
