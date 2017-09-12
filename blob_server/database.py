from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import scoped_session, sessionmaker

from blob_server.config import (
    SQL_USER,
    SQL_DB_NAME,
    SQL_DB_HOST,
    SQL_DB_PORT,
    SQL_PASSWORD
)


def db_uri():
    """
    creates url using defined environment variables
    :return: database password
    """
    return "postgresql://{}:{}@{}:{}/{}".format(
        SQL_USER, SQL_PASSWORD, SQL_DB_HOST, SQL_DB_PORT, SQL_DB_NAME
    )


def get_engine():
    """
    creates the engine
    :return: engine
    """
    engine = create_engine(db_uri())
    return engine


def get_session_registry(engine: Engine):
    """
    :param engine: engine created by get engine
    :return: Session class
    """
    session_factory = sessionmaker(bind=engine)
    Session = scoped_session(session_factory)
    return Session