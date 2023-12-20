
from fastapi import APIRouter
from routers import user_router, login_router, rieltor_router

api_router = APIRouter()


api_router.include_router(user_router.router,  prefix="/auth",tags=["auths"])
api_router.include_router(login_router.router,  prefix="/login",tags=["login"])
api_router.include_router(rieltor_router.router,  prefix="/rieltor",tags=["rieltor"])