from db.NoteDAL import NoteDAL
from schemas.notes import NoteCreate
from schemas.notes import ShowNote
from typing import List


async def _create_new_note(body: NoteCreate, session) -> ShowNote:
    async with session.begin():
        note_dal = NoteDAL(session)
        note = await note_dal.create_note(
            title=body.title,
            author_id=body.author_id,
        )
        return ShowNote(
            id=note.id,
            title=note.title,
            author_id=note.author_id,
        )


async def _get_all_notes_for_user(user_id: int, session) -> List[ShowNote]:
    async with session.begin():
        note_dal = NoteDAL(session)
        notes = await note_dal.get_notes_by_author(author_id=user_id)
        return [
            ShowNote(
                id=note.id,
                title=note.title,
                author_id=note.author_id,
            )
            for note in notes
        ]
