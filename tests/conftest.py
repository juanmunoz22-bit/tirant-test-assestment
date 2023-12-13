import pytest

@pytest.fixture(autouse=True)
def db_session(db):
    yield db.session

