class Game:
    def __init__(self, title):
        self.title = title
        self._results = []
        self._players = []
    
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        if isinstance(new_title, str) and not hasattr(self, 'title'):
            self._title = new_title
        else:
            raise Exception

    def results(self, new_result=None):
        from classes.result import Result
        if isinstance(new_result, Result):
            self._results.append(new_result)
        return self._results
    
    def players(self, new_player=None):
        from classes.player import Player
        if isinstance(new_player, Player):
            self._players.append(new_player)
        return self._players
       
    
    def average_score(self, player):
        my_sum = 0
        num_scores = 0
        for result in player._results:
            if result.game == self:
                my_sum += result.score
                num_scores += 1
        my_sum = my_sum / num_scores
        return my_sum