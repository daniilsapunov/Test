from api.notes import router as router_tasks
from api.users import router as router_users
from api.login import router as router_login

all_routers = [
    router_tasks,
    router_users,
    router_login
]