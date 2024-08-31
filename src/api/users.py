from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from models.users import Users
from schemas.users import UserSchemaAdd, UserSchema
from typing import Annotated
from services.users import UsersService
from api.dependies import users_service

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post("")
async def add_user(
        user: UserSchemaAdd,
        users_service: Annotated[UsersService, Depends(users_service)],
):
    user_id = await users_service.add_user(user)
    return {"user_id": user_id}
