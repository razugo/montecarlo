import numpy as np
import pandas as pd
from lib.configuration import TICKERS, START_DATE, END_DATE
from lib.calculator import Calculator
from lib.scraper import Scraper


class Portfolio:
    def __init__(self, portfolio_number=0):
        # Initialize Data
        self.portfolio_number = portfolio_number
        self.portfolio_weights = None
        self.portfolio_returns = None
        self.portfolio_variance = None
        self.portfolio_standard_deviation = None
        self.portfolio_sharpe = None
        self.result_data_frame = None
        # Generate data
        self.generate_portfolio_weights()

    def generate_portfolio_weights(self):
        weights = np.random.random(len(TICKERS))
        weights /= np.sum(weights)
        self.portfolio_weights = pd.DataFrame([weights], columns=TICKERS, index=[self.portfolio_number])

    def generate_portfolio_data(self, returns: pd.DataFrame, covariance: pd.DataFrame):
        self.portfolio_returns = Calculator.calculate_annual_returns(self.portfolio_weights, returns)
        self.portfolio_variance = Calculator.calculate_annual_variance(self.portfolio_weights, covariance)
        self.portfolio_standard_deviation = np.sqrt(self.portfolio_variance)
        self.portfolio_sharpe = Calculator.calculate_sharpe_ratio(self.portfolio_returns, self.portfolio_variance)
        self.result_data_frame = pd.DataFrame(
            {
                "Expected Return": self.portfolio_returns,
                "Portfolio Variance": self.portfolio_variance,
                "Portfolio Std": self.portfolio_standard_deviation,
                "Sharpe Ratio": self.portfolio_sharpe
            }, index=[self.portfolio_number])
        self.result_data_frame = pd.concat([self.result_data_frame, self.portfolio_weights], axis=1)


if __name__ == '__main__':
    historical_data = Scraper.collect_data(START_DATE, END_DATE)
    historical_returns = Calculator.calculate_returns(historical_data)
    historical_covariance = Calculator.calculate_covariance(historical_returns)
    portfolio = Portfolio()
    portfolio.generate_portfolio_data(historical_returns, historical_covariance)
