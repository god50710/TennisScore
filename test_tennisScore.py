from unittest import TestCase
from TennisScore import TennisScore


class TestTennisScore(TestCase):
    def test_love_all(self):
        self.assertEqual(TennisScore.tennis_judge("Eric", "Maru", 0, 0), "Love All")

