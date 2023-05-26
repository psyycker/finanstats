from finanstats.ticker_service import TickerService

if __name__ == '__main__':
    microsoft_ticker = TickerService("MSFT")
    print(microsoft_ticker.get_history("1mo"))
