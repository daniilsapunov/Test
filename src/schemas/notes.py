from pydantic import BaseModel


class TunedModel(BaseModel):
    class Config:
        """tells pydantic to convert even non dict obj to json"""

        from_attributes = True


class ShowNote(TunedModel):
    id: int
    title: str
    author_id: int


class NoteCreate(BaseModel):
    title: str
    author_id: int
