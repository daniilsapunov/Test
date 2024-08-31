from fastapi import APIRouter, Depends, HTTPException
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

@router.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}


@router.get("/users/me")
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    return current_user