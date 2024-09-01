from pydantic import BaseModel, EmailStr


class TunedModel(BaseModel):
    class Config:
        """tells pydantic to convert even non dict obj to json"""

        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str


class ShowUser(TunedModel):
    id: int
    name: str
    email: EmailStr
    is_active: bool


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
