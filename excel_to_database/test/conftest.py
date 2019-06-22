import pytest
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from ..model.database_manager import Base



@pytest.fixture(scope='session')
def engine():
    return create_engine('postgresql+psycopg2://test:test@localhost:5499/excel_to_db_practice')


@pytest.yield_fixture(scope='session')
def tables(engine):
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)


@pytest.yield_fixture
def dbsession(engine, tables):
    """Returns an sqlalchemy session, and after the test tears down everything properly."""
    session = Session(bind=engine)

    yield session

    Base.metadata.drop_all(engine)
    # roll back the broader transaction
