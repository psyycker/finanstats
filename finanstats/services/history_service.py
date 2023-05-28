import calendar
import datetime

from finanstats.daos.history_dao import HistoryDao
from finanstats.services.ticker_service import TickerService


def is_up_to_date(date):
    now = datetime.date.today()
    if now.weekday() < calendar.SATURDAY:
        compare_date = now
    else:
        days_since_last_friday = (now.weekday() - calendar.FRIDAY + 7) % 7
        compare_date = now - datetime.timedelta(days=days_since_last_friday)

    return date == compare_date


def fetch_history(ticker):
    dao = HistoryDao()
    ticker = TickerService(ticker)
    most_recent = dao.get_most_recent_data_point(ticker.get_ticker_code())
    history = None
    if most_recent is not None and is_up_to_date(most_recent[0]) is False:
        date = most_recent[0]
        history = ticker.get_history_from(date)
    elif most_recent is None:
        history = ticker.get_history()

    if history is not None:
        dao.create_dividends_from_series(history, ticker.get_ticker_code())
    else:
        print(f"skip {ticker.get_ticker_code()}")
