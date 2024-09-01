from typing import Union

from sqlalchemy import and_
from sqlalchemy import select
from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession

from models.users import Users


class UserDAL:
    """Data Access Layer for operating user info"""

    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_user(
            self,
            name: str,
            email: str,
            hashed_password: str,
    ) -> Users:
        new_user = Users(
            name=name,
            email=email,
            hashed_password=hashed_password,
        )
        self.db_session.add(new_user)
        await self.db_session.flush()
        return new_user

    async def delete_user(self, user_id: id) -> Union[id, None]:
        query = (
            update(Users)
            .where(and_(Users.user_id == user_id, Users.is_active == True))
            .values(is_active=False)
            .returning(Users.user_id)
        )
        res = await self.db_session.execute(query)
        deleted_user_id_row = res.fetchone()
        if deleted_user_id_row is not None:
            return deleted_user_id_row[0]

    async def get_user_by_name(self, name: str) -> Union[Users, None]:
        query = select(Users).where(Users.name == name)
        res = await self.db_session.execute(query)
        user_row = res.fetchone()
        if user_row is not None:
            return user_row[0]

    async def get_user_by_email(self, email: str) -> Union[Users, None]:
        query = select(Users).where(Users.email == email)
        res = await self.db_session.execute(query)
        user_row = res.fetchone()
        if user_row is not None:
            return user_row[0]

    async def update_user(self, user_id: id, **kwargs) -> Union[id, None]:
        query = (
            update(Users)
            .where(and_(Users.user_id == user_id, Users.is_active == True))
            .values(kwargs)
            .returning(Users.user_id)
        )
        res = await self.db_session.execute(query)
        update_user_id_row = res.fetchone()
        if update_user_id_row is not None:
            return update_user_id_row[0]
