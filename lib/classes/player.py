class Player:

    all = []

    def __init__(self, username):
        self.username = username
        self._results = []
        self._games_played = []
        self.all.append(self)
    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, new_username):
        if isinstance(new_username, str) and 2 <= len(new_username) <= 16:
            self._username = new_username
        else:
            raise Exception

    def results(self, new_result=None):
        from classes.result import Result
        if isinstance(new_result, Result):
            self._results.append(new_result)
        return self._results
        
    def games_played(self):
        from classes.game import Game
        return [result.game for result in self._results]
    
    def played_game(self, game):
        if [result.game for result in self._results if result.game == game]:
            return True
        else:
            return False
    
    def num_times_played(self, game):
        return len([result.game for result in self._results if result.game == game])
    
    @classmethod
    def highest_scored(cls, game):
        if len(cls.all) == 0:
            return None
        best_player = cls.all[0]
        for player in cls.all:
            if player.played_game(game):
                if game.average_score(player) > game.average_score(best_player):
                    best_player = player
        return best_player
    
        
