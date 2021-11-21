import pathlib
from lib.scraper import Scraper
from lib.calculator import Calculator
from lib.configuration import SIMULATIONS, TOP_X
from lib.portfolio import Portfolio
import pandas as pd
import matplotlib.pyplot as plt


class Simulation:
    def __init__(self, start: str, end: str):
        # initialize data
        self.historical_data = Scraper.collect_data(start, end)
        self.historical_returns = Calculator.calculate_returns(self.historical_data)
        self.historical_covariance = Calculator.calculate_covariance(self.historical_returns)
        self.results = pd.DataFrame(index=['Portfolio Number'])
        self.portfolios = []
        for i in range(SIMULATIONS):
            self.portfolios.append(Portfolio(i))

    def run_simulation(self):
        for portfolio in self.portfolios:
            portfolio.generate_portfolio_data(self.historical_returns, self.historical_covariance)
            self.results = self.results.append(portfolio.result_data_frame)

    def sort_simulation(self):
        self.results = self.results.sort_values("Sharpe Ratio", ascending=False)

    def visualize_data(self):
        # Split off top X
        best = self.results.iloc[:1, :]
        top = self.results.iloc[1:TOP_X, :]
        everything_else = self.results.iloc[TOP_X:, :]
        # Plot both
        best_plot = best.plot.scatter(x="Portfolio Std", y="Expected Return", c='green')
        top_plot = top.plot.scatter(ax=best_plot, x="Portfolio Std", y="Expected Return", c='blue')
        everything_else.plot.scatter(ax=top_plot, x="Portfolio Std", y="Expected Return", c='red')
        plt.show(block=True)

    def save_as_csv(self):
        absolute_path = pathlib.Path(__file__).parent.absolute()
        file_path = "{}/../output/simulation_out.csv".format(absolute_path)
        self.results.to_csv(file_path)
