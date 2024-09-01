from sqlalchemy.ext.asyncio import AsyncSession

from models.notes import Notes


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
