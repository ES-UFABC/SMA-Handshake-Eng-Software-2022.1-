from fastapi import APIRouter

from api.controllers import users_controller as users
from api.controllers import produtos_controller as produtos
from api.controllers import dashboard_controller as dashboard

routes = APIRouter()

routes.include_router(users.router, prefix="/usuarios")
routes.include_router(produtos.router, prefix="/produtos")
routes.include_router(dashboard.router, prefix="/dashboard")
