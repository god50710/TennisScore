SCORE_LIST = ["Love", "Fifteen", "Thirty", "Forty"]


class TennisScore:
    @classmethod
    def tennis_judge(cls, player_1_name, player_2_name, player_1_score, player_2_score):
        if player_1_score != player_2_score:
            if player_1_score > player_2_score and player_1_score > 3:
                if player_1_score - player_2_score > 1:
                    return player_1_name + " Win"
                else:
                    return player_1_name + " Advance"
            elif player_2_score > player_1_score and player_2_score > 3:
                if player_2_score - player_1_score > 1:
                    return player_2_name + " Win"
                else:
                    return player_2_name + " Advance"
            else:
                return SCORE_LIST[player_1_score] + " " + SCORE_LIST[player_2_score]
        elif player_1_score >= 3:
            return "Deuce"
        else:
            return SCORE_LIST[player_1_score] + " All"
