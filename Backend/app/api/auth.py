from fastapi import APIRouter
from app.schemas.user import UserRegister
from app.services.auth_service import register_user
router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register")
def register(user: UserRegister):
    return register_user(user)