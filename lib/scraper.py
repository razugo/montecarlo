import yfinance as yf
import os
import pandas as pd
import pathlib
from lib.configuration import TICKERS


class Scraper:
    @staticmethod
    def collect_data(start: str, end: str) -> pd.DataFrame:
        data_frame = pd.DataFrame()
        for t in TICKERS:
            t_data = Scraper.collect_daily_close_data(t, start, end)
            data_frame = pd.concat([data_frame, t_data], axis=1)
        return data_frame

    @staticmethod
    def collect_daily_close_data(ticker: str, start: str, end: str) -> pd.DataFrame:
        # Example: T, 2010-1-1, 2011-1-25
        # Generate absolute file path
        filename = "{}-{}-{}.json".format(ticker, start, end)
        absolute_path = pathlib.Path(__file__).parent.absolute()
        file_path = "{}/../data/{}".format(absolute_path, filename)
        # Check if file exists
        if os.path.exists(file_path):
            # read and convert json data to dataframe
            with open(file_path, 'r') as f:
                ticker_df = pd.read_json(f)
        else:
            ticker_data = yf.Ticker(ticker)
            ticker_df = ticker_data.history(period='1d', start=start, end=end, timeout=5)
            # Convert to json data and write
            with open(file_path, 'w') as f:
                f.write(ticker_df.to_json())

        # Convert data as needed
        closing_data = ticker_df.Close
        closing_data.rename(ticker, inplace=True)
        closing_data.columns = [ticker]
        return closing_data


if __name__ == '__main__':
    print(Scraper.collect_data("2021-1-1", "2021-1-10"))
