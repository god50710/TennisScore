SCORE_LIST = ["Love", "Fifteen", "Thirty", "Forty"]
ACTION_LIST = [" Advance", " Win"]


class TennisScore:
    @classmethod
    def tennis_judge(cls, game):
        if game.player_1_score != game.player_2_score:
            if game.player_1_score < 4 and game.player_2_score < 4:
                return SCORE_LIST[game.player_1_score] + " " + SCORE_LIST[game.player_2_score]
            else:
                return cls.lead_player_name(game) + ACTION_LIST[cls.game_action(game)]
        elif game.player_1_score >= 3:
            return "Deuce"
        else:
            return SCORE_LIST[game.player_1_score] + " All"

    @classmethod
    def lead_player_name(cls, game):
        return game.player_2_name if cls.player_2_has_higher_score(game) else game.player_1_name

    @classmethod
    def game_action(cls, game):
        return abs(game.player_1_score - game.player_2_score) >> 1

    @classmethod
    def player_2_has_higher_score(cls, game):
        return game.player_2_score > game.player_1_score

