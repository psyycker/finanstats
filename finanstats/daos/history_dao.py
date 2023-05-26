from finanstats.database import Database
from finanstats.model.dividend import Dividend
from sqlalchemy.dialects.postgresql import insert as pg_insert

from finanstats.model.history_data_point import HistoryDataPoint


class HistoryDao:
    _instance = None
    db = Database.get_instance()

    def create_dividends_from_series(self, history, ticker):
        session = self.db.get_session()
        try:
            for date, row in history.iterrows():
                insert_stmt = pg_insert(HistoryDataPoint).values(
                    ticker=ticker,
                    date=date,
                    open=row['Open'],
                    close=row['Close'],
                    high=row['High'],
                    low=row['Low'],
                    volume=row['Volume']
                )
                do_nothing_stmt = insert_stmt.on_conflict_do_nothing(
                    index_elements=['ticker', 'date']
                )
                session.execute(do_nothing_stmt)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()
