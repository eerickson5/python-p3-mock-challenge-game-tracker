class Game:

    all = []

    def __init__(self, title):
        self.title = title
        self.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if type(title) == str and len(title) > 0 and not hasattr(self, "_title"):
            self._title = title

    @classmethod
    def games_by_player(cls, player):
        return [res.game for res in Result.all if res.player == player]

    def results(self):
        return Result.results_by_game(self)

    def players(self):
        all_players = [result.player for result in self.results() if result]
        indi_players = []
        for player in all_players:
            if player not in indi_players:
                indi_players.append(player)
        return indi_players

    def average_score(self, player):
        results = Result.results_by_game(self)
        score_total = 0
        times_played = 0
        for res in results:
            if res.player == player:
                score_total += res.score
                times_played += 1
        return score_total / times_played





class Player:

    all = []

    def __init__(self, username):
        self.username = username
        self.all.append(self)

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if type(username) == str and 2 <= len(username) <= 16 :
            self._username = username

    @classmethod
    def highest_scored(cls, game):
        results = Result.results_by_game(game)
        score_to_player = {}
        scores = []
        for result in results:
            score = result.game.average_score(result.player)
            score_to_player[score] = result.player
            scores.append(score)
        return score_to_player[sorted(scores, reverse=True)[0]]


    def results(self):
        return Result.results_by_player(self)

    def games_played(self):
        all_games = Game.games_by_player(self)
        indi_games = []
        for game in all_games:
            if game not in indi_games:
                indi_games.append(game)
        return indi_games

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        results = Result.results_by_player(self)
        counter = 0
        for res in results:
            if res.game == game:
                counter += 1
        return counter






class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        self.all.append(self)

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        if type(score) == int and 1 <= score <= 5000 and not hasattr(self, "_score"):
            self._score = score

    @classmethod
    def results_by_player(cls, player):
        return [res for res in cls.all if res.player == player]
    
    @classmethod
    def results_by_game(cls, game):
        return [res for res in cls.all if res.game == game]
