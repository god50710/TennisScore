SCORE_LIST = ["Love", "Fifteen", "Thirty", "Forty"]
ACTION_LIST = [" Advance", " Win"]


class TennisScore:
    @classmethod
    def tennis_judge(cls, game):
        return cls.show_same_score(game) if cls.is_same_score(game) else \
            cls.leader_action(game) if cls.is_ready_to_win(game) else cls.show_score(game)

    @classmethod
    def show_score(cls, game):
        return SCORE_LIST[game.player_1_score] + " " + SCORE_LIST[game.player_2_score]

    @classmethod
    def leader_action(cls, game):
        return cls.leader_name(game) + ACTION_LIST[cls.judge_adv_or_win(game)]

    @classmethod
    def leader_name(cls, game):
        return game.player_1_name if cls.player_1_has_higher_score(game) else game.player_2_name

    @classmethod
    def judge_adv_or_win(cls, game):
        return abs(game.player_1_score - game.player_2_score) >> 1

    @classmethod
    def player_1_has_higher_score(cls, game):
        return game.player_1_score > game.player_2_score

    @classmethod
    def is_same_score(cls, game):
        return game.player_1_score == game.player_2_score

    @classmethod
    def is_deuce(cls, game):
        return game.player_1_score >= 3

    @classmethod
    def is_ready_to_win(cls, game):
        return game.player_1_score >= 4 or game.player_2_score >= 4

    @classmethod
    def show_same_score(cls, game):
        return "Deuce" if cls.is_deuce(game) else SCORE_LIST[game.player_1_score] + " All"



