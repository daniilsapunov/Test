from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, DateTime
from datetime import datetime
from db.db import Base
from schemas.notes import NoteSchema


class Notes(Base):
    __tablename__ = "notes"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    def to_read_model(self) -> NoteSchema:
        return NoteSchema(
            id=self.id,
            title=self.title,
            author_id=self.author_id,
            created_at=self.created_at.isoformat(),  # convert datetime to ISO 8601 format
        )
