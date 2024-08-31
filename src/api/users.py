from fastapi import APIRouter, Depends
from schemas.users import UserSchemaAdd
from typing import Annotated
from services.users import UsersService
from api.dependies import users_service

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
