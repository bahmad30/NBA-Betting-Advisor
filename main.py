import pandas as pd


def main():
    df = pd.read_csv(r'/Users/bilaalahmad/Desktop/nba_data.csv', encoding='utf8')
    wins = df[df['Unnamed: 6'] == 'W']
    print(wins)


if __name__ == '__main__':
    main()