import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.database import Base
from app.models.user import User
from app.models.lead import Lead
@pytest.fixture
def db():
    e = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(e)
    return sessionmaker(bind=e)()
