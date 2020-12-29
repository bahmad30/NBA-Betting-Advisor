from operator import itemgetter
import pandas as pd
import scraper

# reads data and utilizes web scraper to create prediction for total points
def main():
    data = pd.read_csv(r'/Users/bilaalahmad/Desktop/clean_nba_data.csv', encoding='utf8')
    pd.to_numeric(data['PV'])
    pd.to_numeric(data['PH'])
    matchups = scraper.main()

    # [team1, team2, total, avg_pts, diff]
    info = []
    # calculates avg points from last
    for index, matchup in enumerate(matchups):
        team1 = str(matchup[0])
        team2 = str(matchup[1])
        total = int(matchup[2])
        relevant_games = data[((data['Visitor'] == team1) | (data['Home'] == team1))
                                  & ((data['Visitor'] == team2) | (data['Home'] == team2))]
        avg_pts = (relevant_games['PV'].sum() + relevant_games['PH'].sum()) / relevant_games['PV'].count()
        avg_pts = round(avg_pts, 3)
        diff = abs(avg_pts - total)
        info.append([team1, team2, total, avg_pts, diff])

    for index, game in enumerate(info, start=1):
        print(f'GAME {index}: {game[0]} vs {game[1]},  TOTAL: {game[2]},  PREDICTED: {game[3]},  DIFF: {game[4]}')


if __name__ == '__main__':
    main()