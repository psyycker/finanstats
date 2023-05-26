import yfinance


class TickerService:
    def __init__(self, ticker_code):
        self.__ticker_code = ticker_code
        self.__data = yfinance.Ticker(self.__ticker_code)

    def get_ticker_code(self):
        return self.__ticker_code

    def get_info(self):
        return self.__data.info

    def get_history(self):
        return self.__data.history(interval="1d", period="max")

    def get_history_from_date(self, start_date):
        return self.__data.history(start=start_date)

    def get_dividends(self):
        return self.__data.dividends
