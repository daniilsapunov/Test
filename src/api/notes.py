from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from services.speller_service import check_text
from api.dependies import notes_service
from services.notes import NotesService
import traceback
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
    try:
        # Проверяем текст заметки
        corrected_text = await check_text(note.title)  # Предполагаем, что текст в поле 'text'

        # Сохраняем заметку с исправленным текстом
        note.title = corrected_text  # Заменяем текст на исправленный
        task_id = await notes_service.add_notes(note)
        return {"task_id": task_id}

    except Exception as e:
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))


@router.get("")
async def get_notes(
        notes_service: Annotated[NotesService, Depends(notes_service)],
        id: int
):
    tasks = await notes_service.get_notes(id)
    return tasks


@router.post("/check/")
async def check_text_endpoint(text: str):
    try:
        corrected_text = await check_text(text)
        return {"corrected_text": corrected_text}
    except Exception as e:
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))
