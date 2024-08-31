from pydantic import BaseModel


class NoteSchema(BaseModel):
    id: int
    title: str
    author_id: int

    class Config:
        from_attributes = True


class NoteSchemaAdd(BaseModel):
    title: str
    author_id: int
