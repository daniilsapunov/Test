from fastapi import APIRouter, Depends
from typing import Annotated

from api.dependies import notes_service
from services.notes import NotesService

from schemas.notes import NoteSchemaAdd
from repositories.notes import NotesRepository

router = APIRouter(
    prefix="/notes",
    tags=["Notes"],
)


@router.post("")
async def add_task(
        note: NoteSchemaAdd,
        notes_service: Annotated[NotesService, Depends(notes_service)],
):
    task_id = await notes_service.add_notes(note)
    return {"task_id": task_id}


@router.get("")
async def get_notes(
        notes_service: Annotated[NotesService, Depends(notes_service)],
        id: int
):
    tasks = await notes_service.get_notes(id)
    return tasks
