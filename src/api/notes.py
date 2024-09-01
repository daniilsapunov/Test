from fastapi import APIRouter, Depends, HTTPException

from api.actions.auth import get_current_user_from_token
from models.users import Users
from services.speller_service import check_text
import traceback
from db.db import get_async_session
from schemas.notes import NoteCreate, ShowNote
from sqlalchemy.ext.asyncio import AsyncSession
from logging import getLogger
from sqlalchemy.exc import IntegrityError
from api.actions.note import _create_new_note

logger = getLogger(__name__)
router = APIRouter(
    prefix="/notes",
    tags=["Notes"],
)


@router.post("", response_model=ShowNote)
async def create_note(
    body: NoteCreate, db: AsyncSession = Depends(get_async_session)
) -> ShowNote:
    try:
        corrected_text = await check_text(body.title)
        body.title = corrected_text
        return await _create_new_note(body, db)
    except IntegrityError as err:
        logger.error(err)
        raise HTTPException(status_code=503, detail=f"Database error: {err}")


@router.get("/get_notes")
async def get_notes_for_user(
    current_user: Users = Depends(get_current_user_from_token),
):
    return {"Success": True, "current_user": current_user}


# @router.get("")
# async def get_notes(
#         notes_service: Annotated[NotesService, Depends(notes_service)],
#         id: int
# ):
#     tasks = await notes_service.get_notes(id)
#     return tasks


@router.post("/check/")
async def check_text_endpoint(text: str):
    try:
        corrected_text = await check_text(text)
        return {"corrected_text": corrected_text}
    except Exception as e:
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))
