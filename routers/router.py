from fastapi import APIRouter
import routers.authentication.auth as auth

api_router = APIRouter()
api_router.include_router(
    auth.router,
    prefix="/auth",
    tags=["authentication"]
)



