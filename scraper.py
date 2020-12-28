import requests
from bs4 import BeautifulSoup


url = 'https://mybookie.ag/sportsbook/nba/'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='accordionBets3')

# iterable containing main games
games = results.find_all('div', class_='game-line py-3')

for game in games:
    # iterable containing buttons for each game
    all_game_buttons = game.find_all('button', class_='lines-odds')
    #
    game_info = all_game_buttons[5]
    print(game_info)
    print('------------new game-------------')
