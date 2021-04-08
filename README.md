# NBA Over/Under Bot

Twitter: https://twitter.com/OverUnderBot

This bot scrapes real-time NBA over/under bets from the web, and uses data from the 2019-2020 NBA season to determine the favorability of a certain over/under pick using a simple predicative model. Each pick is then analyzed and given a 0-10 confidence rating based on the specific matchup data and number of data points. If a pick achieves a confidence rating of at least 7/10, it is considered statistically favorable and automatically posted to Twitter. The syntax of the tweet is adjusted based on the confidence of the pick and 2019-2020 playoff matchups. The success rate of this bot is pending.

Data sources:<br />
Over/under betting lines are from https://mybookie.ag/sportsbook/nba/<br />
2019-2020 NBA data is from https://www.basketball-reference.com/

Project made entirely by Bilaal Ahmad
