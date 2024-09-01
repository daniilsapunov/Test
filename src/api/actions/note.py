from db.NoteDAL import NoteDAL
from schemas.notes import NoteCreate
from schemas.notes import ShowNote


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
