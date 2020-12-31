import requests
from bs4 import BeautifulSoup


# returns list of [TEAM, TEAM, TOTAL] lists
def main():
    url = 'https://mybookie.ag/sportsbook/nba/'
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find(id='accordionBets3')

    # iterable containing main games
    games = results.find_all('div', class_='game-line py-3')
    info = []

    for index, game in enumerate(games, start=1):
        # iterable containing buttons for each game
        all_game_buttons = game.find_all('button', class_='lines-odds')
        # HTML string for button with over under + teams
        game_info = str(all_game_buttons[5])
        # locate team names and total
        team1 = game_info[game_info.find('data-team') + 11: game_info.find('data-team-vs') - 2]
        team2 = game_info[game_info.find('data-team-vs') + 14: game_info.find('data-wager') - 2]
        total = int(game_info[game_info.find('U ') + 2: game_info.find('U ') + 5])
        # print(f'GAME {index}: {team2} @ {team1}, TOTAL: {total}')
        info.append([team1, team2, total])

    return info


if __name__ == '__main__':
    # print the result (list of list) of scraper main
    print(main())
