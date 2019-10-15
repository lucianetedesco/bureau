from contextlib import contextmanager

import singletons
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from core.config import DATABASE_URL


@singletons.GlobalFactory
class Connection:

    def __init__(self):
        self.url = DATABASE_URL
        self._engine = create_engine(self.url, pool_pre_ping=True, pool_recycle=1)
        self._session = scoped_session(sessionmaker(bind=self._engine))

    @contextmanager
    def session(self):

        session = self._session()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()
