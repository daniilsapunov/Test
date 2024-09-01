from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from api.actions.auth import get_current_user_from_token
from api.actions.user import _create_new_user
from db.db import get_async_session
from models.users import Users
from schemas.users import ShowUser, UserCreate
from logging import getLogger

logger = getLogger(__name__)

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)



@router.post("/", response_model=ShowUser)
async def create_user(body: UserCreate, db: AsyncSession = Depends(get_async_session)) -> ShowUser:
    try:
        return await _create_new_user(body, db)
    except IntegrityError as err:
        logger.error(err)
        raise HTTPException(status_code=503, detail=f"Database error: {err}")


@router.get("/test_auth")
async def sample_endpoint(current_user: Users = Depends(get_current_user_from_token),):
    return {"Success": True, 'current_user': current_user}