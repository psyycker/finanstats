from finanstats.daos.history_dao import HistoryDao
from finanstats.services.ticker_service import TickerService


def fetch_history(ticker):
    ticker = TickerService(ticker)
    history = ticker.get_history()
    HistoryDao().create_dividends_from_series(history, ticker.get_ticker_code())
