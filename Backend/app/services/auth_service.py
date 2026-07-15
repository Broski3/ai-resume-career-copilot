from app.schemas.user import UserRegister

def register_user(user: UserRegister):
    return {
        "message": "User registered successfully",
        "name": user.name,
        "email": user.email
    }