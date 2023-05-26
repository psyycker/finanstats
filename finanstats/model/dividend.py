from sqlalchemy import Column, Float, DateTime, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Dividend(Base):
    __tablename__ = 'dividends'

    date = Column(DateTime, primary_key=True)
    ticker = Column(String, primary_key=True)
    amount = Column(Float)
