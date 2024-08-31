from schemas.notes import NoteSchemaAdd
from utils.repository import AbstractRepository
from models.notes import Notes


class NotesService:
    def __init__(self, notes_repo: AbstractRepository):
        self.notes_repo = notes_repo()

    async def add_notes(self, note: NoteSchemaAdd):
        notes_dict = note.model_dump()
        note_id = await self.notes_repo.add_one(notes_dict)
        return note_id

    async def get_notes(self, id: int = None):
        tasks = await self.notes_repo.find_all(Notes.author_id == id)
        return tasks
