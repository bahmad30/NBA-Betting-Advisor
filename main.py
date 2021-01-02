from operator import itemgetter
import pandas as pd
import scraper
import twitterbot

# request to post to twitter if program is run
activate_tbot = True

# minimum rating to be posted on twitter
tweet_threshold = 7


# reads data and utilizes web scraper to create prediction for total points
def main():
    data = pd.read_csv(r'/Users/bilaalahmad/Desktop/clean_nba_data.csv', encoding='utf8')
    pd.to_numeric(data['PV'])
    pd.to_numeric(data['PH'])
    matchups = scraper.main()

    # [team1, team2, total, avg_pts, diff, o/u, gp, conf]
    info = []
    # calculates avg points from last
    for index, matchup in enumerate(matchups):
        team1 = str(matchup[0])
        team2 = str(matchup[1])
        total = float(matchup[2])
        relevant_games = data[((data['Visitor'] == team1) | (data['Home'] == team1))
                              & ((data['Visitor'] == team2) | (data['Home'] == team2))]
        games_played = relevant_games['PV'].count()
        avg_pts = (relevant_games['PV'].sum() + relevant_games['PH'].sum()) / games_played
        avg_pts = round(avg_pts, 1)
        if avg_pts > total:
            ou = 'O'
        else:
            ou = 'U'
        diff = round(abs(avg_pts - total), 1)
        conf = confidence(games_played, diff)
        info.append([team1, team2, total, avg_pts, diff, ou, games_played, conf])

    # sort data
    info = ranker(info)
    # filter based on tweet threshold
    tweet_data = []
    for game in info:
        if game[7] >= tweet_threshold:
            tweet_data.append(game)
    print('------PICKS------')
    for index, game in enumerate(tweet_data, start=1):
        print(f'G{index}: {game[0]} vs {game[1]},  TOTAL: {game[2]},  PREDICTED: {game[3]},  DIFF: {game[4]}'
              f' {game[5]},  GP: {game[6]},  CONF: {game[7]}')

    # post to twitter
    if activate_tbot:
        print('------TWEETS------')
        twitterbot.main(tweet_data)


# gives a confidence rating up to 10 for over/under based on games played and diff
def confidence(games_played, diff):
    rating = 0
    # give 1-5 rating based on playoff opp, div opp, non-div opp
    if games_played > 4:
        rating += 5
    elif games_played == 4:
        rating += 4
    elif games_played == 3:
        rating += 3
    else:
        rating += 2
    # give 1-5 rating based on diff
    if diff >= 13.5:
        rating += 5
    elif 9.5 <= diff < 13.5:
        rating += 4
    elif 6.5 <= diff < 9.5:
        rating += 3
    elif 4.5 <= diff < 6.5:
        rating += 2
    else:
        rating += 1
    return rating


def ranker(info):
    info = sorted(info, key=itemgetter(7), reverse=True)
    print('------MATCHUPS------')
    for index, game in enumerate(info, start=1):
        print(f'G{index}: {game[0]} vs {game[1]},  TOTAL: {game[2]},  PREDICTED: {game[3]},  DIFF: {game[4]}'
              f' {game[5]},  GP: {game[6]},  CONF: {game[7]}')
    return info


if __name__ == '__main__':
    main()
