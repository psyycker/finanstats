from finanstats.database import Database
from finanstats.model.Ticker import Ticker
from sqlalchemy.dialects.postgresql import insert as pg_insert


class TickersDao:
    _instance = None
    db = Database.get_instance()

    def add_tickers_from_df(self, tickers):
        session = self.db.get_session()
        try:
            for index, row in tickers.iterrows():
                name = row['Name']
                insert_stmt = pg_insert(Ticker).values(
                    name=name
                )
                do_nothing_stmt = insert_stmt.on_conflict_do_nothing(
                    index_elements=['name']
                )
                session.execute(do_nothing_stmt)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

    def get_all_ticker(self):
        session = self.db.get_session()
        try:
            tickers = session.query(Ticker).all()
        except Exception as e:
            print(f"An error occured: {e}")
            session.rollback()
            return None
        finally:
            session.close()

        return tickers
