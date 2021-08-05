from __future__ import print_function
from os import strerror
import datetime
from dataclasses import dataclass

# Discord Imports for Embeds
from discord import Embed

# MLB Game imports
import mlbgame 
from mlbgame.game import GameScoreboard

@dataclass
class ScoreBoard():

    # Away Team
    away_team_name: str
    away_team_errors: str
    away_team_hits: int
    away_team_runs: int
    #away_team_pitchers: list[Stats]
    
    # Home Team
    home_team_name: str
    home_team_errors: str
    home_team_hits: int
    home_team_runs: int
    #home_team_pitchers: list[Stats]

    # Game Info
    date: datetime.datetime
    game_id: str
    game_status: str
    game_leauge: str
    game_start_time: datetime.datetime
    events: list
    score: str

    def __init__(self, mlb_game_sb: GameScoreboard) -> None:
        self.away_team_errors = mlb_game_sb.away_team_errors
        self.away_team_hits   = int(mlb_game_sb.away_team_hits)
        self.away_team_runs   = int(mlb_game_sb.away_team_hits)
        self.away_team_name   = mlb_game_sb.away_team

        self.home_team_errors = mlb_game_sb.home_team_errors
        self.home_team_hits   = int(mlb_game_sb.home_team_runs)
        self.home_team_runs   = int(mlb_game_sb.home_team_hits)
        self.home_team_name   = mlb_game_sb.home_team
        self.date             = mlb_game_sb.date
        self.game_id          = mlb_game_sb.game_id
        self.game_leauge      = mlb_game_sb.game_league
        self.game_start_time  = mlb_game_sb.game_start_time
        self.game_status      = mlb_game_sb.game_status
        self.score            = mlb_game_sb.nice_score()
        self.events            = []

    def _populate_events(self):
        try:
            self.events = mlbgame.game_events(self.game_id)
        
        except IndexError as e:                
            print("Index error getting events: ", e)
    
    def _get_new_events(self):
        new_events = []
        try:
            game_events = mlbgame.game_events(self.game_id)
            if len(game_events) == len(self.events):
                pass
            else:
                pass
        except:
            pass
                
def generate_active_game_list_embed(games_to_format: list[ScoreBoard]) -> Embed:
    active_games = []
    for game in games_to_format:
        if game.game_status != "IN_PROGRESS":
            continue
        active_games.append(game)
    return generate_game_list_embed(active_games)

def generate_game_list_embed(games_to_format: list[ScoreBoard]) -> Embed:
    game_embed = Embed()
    for games in games_to_format:
        
        game_embed.add_field(value=games.score, inline=False,
                name=f"{games.away_team_name} at {games.home_team_name} -- [{games.game_status}]")
        
    return game_embed


def get_games_today():
    """ 
        Grabs all of the games that are happening today and yesterday. 
        Two days are grabbed to handle games running past midnight

        @TODO The MLB day starts at 5am EST. 
    """
    td = datetime.datetime.today()
    yd = datetime.datetime.today() - datetime.timedelta(days=1)

    games_yesterday = mlbgame.day(year=yd.year, month=yd.month, day=yd.day)
    games_today = mlbgame.day(year=td.year, month=td.month, day=td.day)
    
    games = games_today + games_yesterday
    score_boards = []
    for g in games:
        sb = ScoreBoard(g)
        score_boards.append(sb)
    
    return score_boards

if __name__ == "__main__":
    for s in get_games_today():
        if s.game_status == "IN_PROGRESS":
            print(s)
        elif s.game_status == "FINAL":
            print(s)
        elif s.game_status == "PRE_GAME":
            print(s)
        else:
            print(f"Unknown game status: {s.game_status}")

        print(s.game_status)
