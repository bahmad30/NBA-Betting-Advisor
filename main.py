import pandas as pd
import scraper


def main():
    data = pd.read_csv(r'/Users/bilaalahmad/Desktop/clean_nba_data.csv', encoding='utf8')
    pd.to_numeric(data['PV'])
    pd.to_numeric(data['PH'])
    matchups = scraper.main()

    for index, matchup in enumerate(matchups):
        team1 = str(matchups[index][0])
        team2 = str(matchups[index][1])
        total = int(matchups[index][2])
        relevant_games = data[((data['Visitor'] == team1) | (data['Home'] == team1))
                                  & ((data['Visitor'] == team2) | (data['Home'] == team2))]
        avg_pts = (relevant_games['PV'].sum() + relevant_games['PH'].sum()) / relevant_games['PV'].count()
        avg_pts = round(avg_pts, 3)
        diff = abs(avg_pts - total)

        print(f'GAME: {team1} vs {team2}, TOTAL: {total}, PREDICTED: {avg_pts}, DIFF: {diff}')


if __name__ == '__main__':
    main()


