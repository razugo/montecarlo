import numpy as np

np.random.seed(10)

RISK_FREE_RATE = 0.02
ANNUAL_TRADING_DAYS = 252
TOP_X = 10

# Top 7 etfs
# TICKERS = ["SPY", "VTWO", "IJH", "VEU", "VWO", "VT", "AGG"]
# Vanguard ETFs
TICKERS = [
    "ESGV",
    "VUG",
    "VV",
    "MGC",
    "MGK",
    "MGV",
    "VONE",

    "VONG",
    "VONV",
    "VTHR",
    "VOO",
    "VOOG",
    "VOOV",
    "VTI",

    "VXF",
    "VO",
    "VOT",
    "VOE",
    "IVOO",
    "IVOG",

    "IVOV",
    "VTWO",
    "VTWG",
    "VTWV",
    "VIOO",
    "VIOG",

    "VBK",
    "VBR",
    "BNDW",
    "BNDX",
    "VWOB",
    "VT",
    
    "VEU",
    "VSS",
    "VEA",
    "VGK",
    "VPL",

    "VXUS",
    "VWO",
]
START_DATE = '2000-1-1'
END_DATE = '2020-2-1'
SIMULATION_YEARS = 10
SIMULATIONS = 1000

SIMULATION_DAYS = SIMULATION_YEARS*ANNUAL_TRADING_DAYS
