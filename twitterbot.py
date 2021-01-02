import tweepy
import keys

# tweet if true
tweet_it = False


# formats and posts tweet
def main(tweet_data):
    auth = tweepy.OAuthHandler(keys.CONSUMER_KEY, keys.CONSUMER_SECRET)
    auth.set_access_token(keys.ACCESS_KEY, keys.ACCESS_SECRET)
    api = tweepy.API(auth)

    for game in tweet_data:
        # clean and format data
        if game[5] == 'O':
            ou = ['over', 'less']
        else:
            ou = ['under', 'more']
        if game[7] == 7:
            wording = ['Consider taking', '.', 'a solid']
        elif game[7] == 8:
            wording = ['Take', '!', 'a noteworthy']
        elif game[7] == 9:
            wording = ['Take', '!', 'an outstanding']
        else:
            wording = ['Definitely take', '!', 'a rare, perfect']

        team1 = game[0].split()[len(game[0].split()) - 1]
        team2 = game[1].split()[len(game[1].split()) - 1]
        total = dropzero(game[2])
        diff = dropzero(game[4])
        pred = dropzero(game[3])
        # tweet body
        tweet = f'{wording[0]} the {ou[0]} for the {team1} vs {team2} game{wording[1]} The current total is {total}, ' \
                f'which is {diff} {ou[1]} than our predicted total. ' \
                f'This pick\'s confidence rating is {wording[2]} {game[7]}/10.'

        if tweet_it:
            try:
                api.update_status(tweet)
                print(f'TWEETED: {tweet}')
            except tweepy.error.TweepError as err:
                print(f'DUPLICATE ERROR: {err}')
                print(f'NOT TWEETED: {tweet}')
            except Exception as e:
                print(f'ERROR: {e}')
                print(f'NOT TWEETED: {tweet}')
        else:
            print(f'NOT TWEETED: {tweet}')


# drop .0 from a number
def dropzero(num):
    if num - int(num) == 0:
        return int(num)
    else:
        return num
