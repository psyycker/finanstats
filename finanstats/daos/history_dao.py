from sqlalchemy import text
from finanstats.database import Database
from sqlalchemy.dialects.postgresql import insert as pg_insert

from finanstats.model.history_data_point import HistoryDataPoint


class HistoryDao:
    _instance = None
    db = Database.get_instance()

    def get_all_history_for_ticker(self, ticker):
        session = self.db.get_session()
        try:
            return session.execute(text("""
                SELECT date, open, close, high, low, volume FROM history_data_points WHERE ticker = :ticker ORDER BY date
            """), {"ticker": ticker})
        except:
            raise
        finally:
            session.close()

    def get_most_recent_data_point(self, ticker):
        session = self.db.get_session()
        try:
            result = session.execute(
                text("""
                SELECT MAX(date) as latest_date FROM history_data_points WHERE ticker = :ticker
            """), {"ticker": ticker})
            return result.fetchone()
        except:
            raise
        finally:
            session.close()

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
