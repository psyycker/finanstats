from finanstats.daos.tickers_dao import TickersDao
from finanstats.tickers.tickers_fetcher import fetch_and_save_tickers

if __name__ == '__main__':
    fetch_and_save_tickers()
    tickers = TickersDao().get_all_ticker()
    print()
