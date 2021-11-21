import numpy as np
import pandas as pd
from lib.configuration import RISK_FREE_RATE, SIMULATION_DAYS
from lib.scraper import Scraper


class Calculator:
    @staticmethod
    def calculate_returns(ticker_data: pd.DataFrame):
        # Use pandas percent change function
        return ticker_data.pct_change()

    @staticmethod
    def calculate_covariance(returns: pd.DataFrame):
        # Use pandas covariance function
        return returns.cov()

    @staticmethod
    def calculate_annual_returns(weights: pd.DataFrame, returns: pd.DataFrame):
        returns_mean = returns.mean().to_frame()
        result_data = weights.dot((returns_mean * SIMULATION_DAYS).to_numpy())
        return result_data.to_numpy()[0][0]

    @staticmethod
    def calculate_annual_variance(weights: pd.DataFrame, covariance: pd.DataFrame):
        weights_dot_covariance = weights.dot((covariance * SIMULATION_DAYS).to_numpy())
        result_dot_weights = weights_dot_covariance.dot(weights.transpose().to_numpy())
        return result_dot_weights.to_numpy()[0][0]

    @staticmethod
    def calculate_sharpe_ratio(portfolio_returns: float, portfolio_variance: float):
        # risk free rate pulled from configuration
        return (portfolio_returns - RISK_FREE_RATE) / np.sqrt(portfolio_variance)


if __name__ == '__main__':
    data = Scraper.collect_data("2021-1-1", "2021-1-10")
    ret = Calculator.generate_returns(data)
    cov = Calculator.generate_covariance(ret)
