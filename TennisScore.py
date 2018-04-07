SCORE_LIST = ["Love", "Fifteen", "Thirty", "Forty"]


class TennisScore:
    @classmethod
    def tennis_judge(cls, player_1, player_2, player_1_score, player_2_score):
        if player_1_score != player_2_score:
            return SCORE_LIST[player_1_score] + " " + SCORE_LIST[player_2_score]
        elif player_1_score >= 3:
            return "Deuce"
        else:
            return SCORE_LIST[player_1_score] + " All"
