from typing import Union
from uuid import UUID

from schemas.users import ShowUser
from schemas.users import UserCreate
from db.UserDAL import UserDAL
from models.users import Users
from utils.utils import Hasher


async def _create_new_user(body: UserCreate, session) -> ShowUser:
    async with session.begin():
        user_dal = UserDAL(session)
        user = await user_dal.create_user(
            name=body.name,
            email=body.email,
            hashed_password=Hasher.hash_password(body.password),
        )
        return ShowUser(
            id=user.id,
            name=user.name,
            email=user.email,
            is_active=user.is_active,
        )


async def _delete_user(user_id, session) -> Union[UUID, None]:
    async with session.begin():
        user_dal = UserDAL(session)
        deleted_user_id = await user_dal.delete_user(
            user_id=user_id,
        )
        return deleted_user_id


async def _update_user(
        updated_user_params: dict, user_id: UUID, session
) -> Union[UUID, None]:
    async with session.begin():
        user_dal = UserDAL(session)
        updated_user_id = await user_dal.update_user(
            id=user_id, **updated_user_params
        )
        return updated_user_id


# async def _get_user_by_id(user_id, session) -> Union[Users, None]:
#     async with session.begin():
#         user_dal = UserDAL(session)
#         user = await user_dal.get_user_by_id(
#             id=user_id,
#         )
#         if user is not None:
#             return user
