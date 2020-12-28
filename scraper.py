import requests
from bs4 import BeautifulSoup


url = 'https://mybookie.ag/sportsbook/nba/'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

game = soup.find(id='11343535_543_to')

print(game)


