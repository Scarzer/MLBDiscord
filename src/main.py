from __future__ import print_function
from os import strerror
import mlbgame 
import datetime
from dataclasses import dataclass
from mlbgame.events import Inning

from mlbgame.stats import Stats 
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
                



games = mlbgame.day(year=2021, month=8, day=3)

for g in games:
    try:
        sb = ScoreBoard(g)
        print(sb)
        print(g.nice_score())
        # game_events = mlbgame.game_events(g.game_id)
        # for ev in game_events:
        #     print(ev.nice_output())
        #     print("Top")
        #     for t in ev.top:
        #         print(t.__dict__)
        #     print("Bott")
        #     for b in ev.bottom:
        #         print(b.__dict__)
        print("==============")

    except IndexError as e:
        print(f"Can't print out game events:{e}")

