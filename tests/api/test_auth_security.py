import asyncio

from app.api import auth
from app.models.user import UserRole
from app.schemas.user import UserCreate


class _Result:
    def scalar_one_or_none(self):
        return None


class _Session:
    def __init__(self):
        self.added = None

    async def execute(self, _query):
        return _Result()

    def add(self, user):
        self.added = user

    async def commit(self):
        pass

    async def refresh(self, _user):
        pass


class _User:
    email = object()

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


def test_public_registration_always_creates_team_member(monkeypatch):
    class _Query:
        def where(self, _condition):
            return self

    monkeypatch.setattr(auth, "select", lambda _model: _Query())
    monkeypatch.setattr(auth, "User", _User)
    monkeypatch.setattr(auth, "get_password_hash", lambda _password: "hash")
    session = _Session()

    user = UserCreate(email="member@example.com", password="password123", role="super_admin")
    asyncio.run(auth.register(user, session))

    assert session.added.role is UserRole.TEAM_MEMBER
