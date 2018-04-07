SCORE_LIST = ["Love", "Fifteen", "Thirty", "Forty"]


class TennisScore:
    @classmethod
    def tennis_judge(cls, player_1_name, player_2_name, player_1_score, player_2_score):
        if player_1_score != player_2_score:
            if player_1_score > player_2_score and player_1_score > 3:
                return player_1_name + " Advance"
            else:
                return SCORE_LIST[player_1_score] + " " + SCORE_LIST[player_2_score]
        elif player_1_score >= 3:
            return "Deuce"
        else:
            return SCORE_LIST[player_1_score] + " All"
