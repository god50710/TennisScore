class TennisScore:
    @classmethod
    def tennis_judge(cls, player_1, player_2, player_1_score, player_2_score):
        if player_2_score == 1:
            return "Love Fifteen"
        else:
            return "Love All"
