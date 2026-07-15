from app.schemas.user import UserRegister

users = []

def find_user_by_email(email: str):
    for user in users:
        if user.email==email:
            return user 
    return None


def save_user(user:UserRegister):
    users.append(user)