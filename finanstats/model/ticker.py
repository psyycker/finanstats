from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String

Base = declarative_base()


class Ticker(Base):
    __tablename__ = 'tickers'

    name = Column(String, primary_key=True)
