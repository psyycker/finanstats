import requests
import pandas as pd
from io import StringIO

from finanstats.daos.tickers_dao import TickersDao

fetch_tickers_cvs_url = "https://www.cboe.com/us/equities/market_statistics/listed_symbols/csv"

def fetch_and_save_tickers():
    response = requests.get(fetch_tickers_cvs_url)
    response.raise_for_status()
    data = response.text
    data_io = StringIO(data)
    df = pd.read_csv(data_io)
    TickersDao().add_tickers_from_df(df)
