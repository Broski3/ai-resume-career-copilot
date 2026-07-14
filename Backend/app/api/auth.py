from fastapi import APIRouter
from app.schemas.user import UserRegister

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register")
def register(user: UserRegister):
    return {
        "message": "User received successfully",
        "user": user
    }