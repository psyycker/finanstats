from finanstats.database import Database
from finanstats.model.dividend import Dividend


class DividendDao:
    _instance = None
    db = Database.get_instance()

    def create_dividend(self, ticker, date, amount):
        session = self.db.get_session()
        try:
            entry = Dividend(
                date=date,
                amount=amount,
                ticker=ticker
            )
            session.add(entry)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

    def create_dividends_from_series(self, dividends, ticker):
        session = self.db.get_session()
        try:
            for date, dividend in dividends.items():
                entry = Dividend(
                    date=date,
                    amount=dividend,
                    ticker=ticker
                )
                session.add(entry)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()
