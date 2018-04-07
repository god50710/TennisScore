SCORE_LIST = ["All", "Fifteen", "Thirty", "Forty"]


class TennisScore:
    @classmethod
    def tennis_judge(cls, player_1, player_2, player_1_score, player_2_score):
        return "Love " + SCORE_LIST[player_2_score]
