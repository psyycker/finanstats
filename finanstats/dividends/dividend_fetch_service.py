from finanstats.daos.dividend_dao import DividendDao
from finanstats.database import Database
from finanstats.ticker_service import TickerService


def fetch_dividends(ticker):
    ticker_service = TickerService(ticker)
    dividends = ticker_service.get_dividends()
    DividendDao().create_dividends_from_series(dividends, ticker)


