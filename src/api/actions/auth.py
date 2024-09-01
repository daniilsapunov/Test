from typing import Union

from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from jose import JWTError
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from settings import settings
from db.UserDAL import UserDAL
from models.users import Users
from db.db import get_async_session
from utils.utils import Hasher

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login/token")


async def _get_user_by_name_for_auth(name: str, session: AsyncSession):
    async with session.begin():
        user_dal = UserDAL(session)
        return await user_dal.get_user_by_name(
            name=name,
        )


async def authenticate_user(
        name: str, password: str, db: AsyncSession
) -> Union[Users, None]:
    user = await _get_user_by_name_for_auth(name=name, session=db)
    if user is None:
        return
    if not Hasher.verify_password(password, user.hashed_password):
        print(password, user.hashed_password)
        return
    return user


async def get_current_user_from_token(
        token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_async_session)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        print(payload)
        name: str = payload.get("sub")
        if name is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = await _get_user_by_name_for_auth(name=name, session=db)
    if user is None:
        raise credentials_exception
    return user
