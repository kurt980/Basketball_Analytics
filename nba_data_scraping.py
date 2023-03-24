##Scraping NBA data
import pandas as pd

from nba_api.stats.static import players
from nba_api.stats.static import teams

player_dict = players.get_players()
team_dict = teams.get_teams()

bron = [player for player in player_dict if player['full_name'] == 'LeBron James']
gsw = [team for team in team_dict if team['full_name'] == 'Golden State Warriors']

from nba_api.stats.endpoints import playergamelog

gamelog_bron = playergamelog.PlayerGameLog(player_id='2544',season='2017')

gamelog_bron_df = gamelog_bron.get_data_frames()[0]

print(gamelog_bron_df.head())
