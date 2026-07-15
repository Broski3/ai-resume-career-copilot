from app.schemas.user import UserRegister
from app.repository.user_repository import (find_user_by_email,save_user)
def register_user(user: UserRegister):
    existing_user = find_user_by_email(user.email)

    if existing_user:
        return{
            "message":"Email already exists"
        }
    
    save_user(user)

    return{
        "meassage":"User Registered Successfully",
        "name":user.name,
        "email":user.email
    }