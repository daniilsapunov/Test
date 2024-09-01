from sqlalchemy import Column, Integer, String, Boolean
from db.db import Base
from schemas.users import ShowUser


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    hashed_password = Column(String, nullable=False)

    def to_read_model(self) -> ShowUser:
        return ShowUser(
            id=self.id,
            name=self.name,
            email=self.email,
            is_active=self.is_active,
            hashed_password=self.hashed_password,  # don't expose the hashed password in the response
        )
