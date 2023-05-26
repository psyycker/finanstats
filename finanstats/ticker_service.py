import yfinance


class TickerService:
    def __init__(self, ticker_code):
        self.__ticker_code = ticker_code
        self.__data = yfinance.Ticker(self.__ticker_code)

    def get_ticker_code(self):
        return self.__ticker_code

    def get_info(self):
        return self.__data.info

    def get_history(self, period):
        return self.__data.history(period)

    def get_dividends(self):
        return self.__data.dividends
