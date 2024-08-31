from models.notes import Notes
from utils.repository import SQLAlchemyRepository


class NotesRepository(SQLAlchemyRepository):
    model = Notes
