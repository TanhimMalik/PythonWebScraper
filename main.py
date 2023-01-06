import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = 'https://www.basketball-reference.com/leagues/NBA_2022_per_game.html'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

stats_table = soup.find('table', {'id': 'per_game_stats'})

# Extract the player stats
player_stats = []
for tr in stats_table.find_all('tr')[1:]:
    player_stats.append([td.text for td in tr.find_all('td')])

# Create the pandas DataFrame
df = pd.DataFrame(player_stats, columns=['Player', 'Pos', 'Age', 'Tm', 'G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%', '2P', '2PA', '2P%', 'eFG%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS'])

# Select the columns of interest and sort by points in descending order
df = df[['Player', 'Pos', 'PTS', 'AST', 'TRB']].sort_values(by='PTS', ascending=False)

# Save the DataFrame to a CSV file
df.to_csv('player_stats.csv', index=False, encoding='utf-8')
