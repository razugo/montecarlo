import numpy as np

np.random.seed(10)

RISK_FREE_RATE = 0.02
ANNUAL_TRADING_DAYS = 252
TOP_X = 10

TICKERS = ["SPY", "VTWO", "IJH", "VEU", "VWO", "VT", "AGG"]
START_DATE = '2000-1-1'
END_DATE = '2020-2-1'
SIMULATION_YEARS = 1
SIMULATIONS = 10000

SIMULATION_DAYS = SIMULATION_YEARS*ANNUAL_TRADING_DAYS