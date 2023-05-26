from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Date, Float, Numeric

Base = declarative_base()


class HistoryDataPoint(Base):
    __tablename__ = 'history_data_points'

    ticker = Column(String, primary_key=True)
    date = Column(Date, primary_key=True)
    open = Column(Float)
    close = Column(Float)
    high = Column(Float)
    low = Column(Float)
    volume = Column(Numeric)
