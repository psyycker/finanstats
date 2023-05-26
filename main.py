from finanstats.daos.tickers_dao import TickersDao
from finanstats.dividends.dividend_fetch_service import fetch_dividends
from finanstats.tickers.tickers_fetcher import fetch_and_save_tickers


def update_dividends(tickers):
    total = len(tickers)
    for index, ticker in enumerate(tickers):
        print(f"{index}/{total}")
        fetch_dividends(ticker.name)


if __name__ == '__main__':
    fetch_and_save_tickers()
    tickers = TickersDao().get_all_ticker()
    update_dividends(tickers)
