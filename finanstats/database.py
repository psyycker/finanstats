from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class Database:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance._session_factory = sessionmaker(bind=create_engine('postgresql://finanstats_user:finanstats_password@localhost:5444/finanstats'),
                                                          expire_on_commit=False)
            cls._instance._Session = scoped_session(cls._instance._session_factory)
        return cls._instance

    def get_session(self):
        return self._Session()

    @staticmethod
    def get_instance():
        if Database._instance is None:
            Database()
        return Database._instance
