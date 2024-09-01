from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from models.notes import Notes
from sqlalchemy import select


class NoteDAL:
    """Data Access Layer for operating user info"""

    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_note(
        self,
        title: str,
        author_id: int,
    ) -> Notes:
        new_note = Notes(
            title=title,
            author_id=author_id,
        )
        self.db_session.add(new_note)
        await self.db_session.flush()
        return new_note

    async def get_notes_by_author(self, author_id: int):
        query = select(Notes).where(Notes.author_id == author_id)
        result = await self.db_session.execute(query)
        return result.scalars().all()
