import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (14, 7)
plt.rcParams['axes.grid'] = True

def missingTimestamp(df):
    df = df.sort_values('Timestamp')

    expected_freq = pd.to_timedelta("5s")
    actual_gaps = df['Timestamp'].diff().value_counts()

    print()
    print("Most common timestamp gaps:")
    print(actual_gaps)

    if len(actual_gaps) == 1 and actual_gaps.index[0] == expected_freq:
        print("✅ Dataset is perfectly continuous at 5-second intervals.")
    else:
        print("⚠ Irregular gaps detected.")


def visualizingPrice(df):
    plt.plot(df['Timestamp'], df['Close'], linewidth=0.7)
    plt.title("Bitcoin Close Price (5-Second Intervals)")
    plt.xlabel("Time")
    plt.ylabel("Price (USDT)")
    plt.show()


def candlestick(df):
    sample = df.iloc[:2000].copy()

    plt.plot(sample['Timestamp'], sample['Close'], label='Close', linewidth=0.7)
    plt.fill_between(sample['Timestamp'], sample['Low'], sample['High'],
                     alpha=0.5, color='red', label='High-Low range')

    plt.title("Bitcoin OHLC Visualization — First 2000 Intervals")
    plt.xlabel("Time")
    plt.ylabel("Price")
    plt.legend()
    plt.show()


def movingAverage(df):
    sample = df.iloc[:2000].copy()
    sample['SMA50'] = sample['Close'].rolling(50).mean()
    sample['SMA200'] = sample['Close'].rolling(200).mean()

    plt.plot(sample['Timestamp'], sample['Close'], linewidth=0.7, label='Close')
    plt.plot(sample['Timestamp'], sample['SMA50'], label='SMA 50')
    plt.plot(sample['Timestamp'], sample['SMA200'], label='SMA 200')

    plt.legend()
    plt.title("Close Price with Moving Averages")
    plt.show()


def corrMatrix(df):
    corr = df[['Open', 'High', 'Low', 'Close', 'Volume', 'QuoteVolume']].corr()
    print()
    print("Correlation matrix:")
    print(corr)


def main():
    df = pd.read_csv(
        "/kaggle/input/bitcoin-historical-data-ohlcv-5-second-interval/BTCUSDT_2025_01_01-07_avg5s.csv",
        sep=';',
        parse_dates=['Timestamp']
    )

    print(df.head())

    missingTimestamp(df)
    candlestick(df)
    movingAverage(df)
    corrMatrix(df)


if __name__ == "__main__":
    main()
