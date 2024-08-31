from repositories.notes import NotesRepository
from services.notes import NotesService
from repositories.users import UsersRepository
from services.users import UsersService


def notes_service():
    return NotesService(NotesRepository)


def users_service():
    return UsersService(UsersRepository)
