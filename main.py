import pandas as pd


def main():
    df = pd.read_csv(r'/Users/bilaalahmad/Desktop/all_nba_data.csv', encoding='utf8')
    print(df)


if __name__ == '__main__':
    main()
