from app.schemas.user import UserRegister
from app.repository.user_repository import (find_user_by_email,save_user)
from app.utils.security import hash_password
from app.repository.user_repository import find_user_by_email
from app.utils.security import verify_password
from app.utils.security import create_access_token

def register_user(user: UserRegister):
    existing_user = find_user_by_email(user.email)

    if existing_user:
        return{
            "message":"Email already exists"
        }
    #hash the password
    user.password=hash_password(user.password)
    save_user(user)

    return{
        "meassage":"User Registered Successfully",
        "name":user.name,
        "email":user.email
    }
def login_user(login_data):
    user = find_user_by_email(login_data.email)

    if not user:
        return {
            "message": "Invalid Email or Password"
        }

    is_valid = verify_password(
        login_data.password,
        user.password
    )

    if is_valid:
        access_token = create_access_token(
            {
                "sub": user.email
            }
        )

        return {
            "message": "Login Successful",
            "access_token": access_token,
            "token_type": "bearer"
        }

    return {
        "message": "Invalid Email or Password"
    }