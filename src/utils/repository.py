from abc import ABC, abstractmethod

from sqlalchemy import insert, select

from db.db import async_session_maker
from utils.utils import Hasher


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one():
        raise NotImplementedError

    @abstractmethod
    async def find_all():
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def add_one(self, data: dict) -> int:
        async with async_session_maker() as session:
            data["hashed_password"] = Hasher.hash_password(data["password"])
            stmt = insert(self.model).values(**data)
            res = await session.execute(stmt)
            await session.commit()
            return res.inserted_primary_key[0]

    async def find_all(self, *filter):
        async with async_session_maker() as session:
            stmt = select(self.model).filter(*filter)
            res = await session.execute(stmt)
            res = [row[0].to_read_model() for row in res.all()]
            return res
