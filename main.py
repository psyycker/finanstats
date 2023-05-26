from finanstats.daos.tickers_dao import TickersDao
from finanstats.services.dividend_fetch_service import fetch_dividends
from finanstats.services.history_service import fetch_history


def update_dividends(tickers):
    print('updating dividends')
    total = len(tickers)
    for index, ticker in enumerate(tickers):
        print(f"{index}/{total}")
        fetch_dividends(ticker.name)

def update_history(tickers):
    print('Updating history')
    total = len(tickers)
    for index, ticker in enumerate(tickers):
        print(f"{index}/{total}")
        fetch_history(ticker.name)


if __name__ == '__main__':
    # fetch_and_save_tickers()
    tickers = TickersDao().get_all_ticker()
    update_history(tickers)
    # update_dividends(tickers)
