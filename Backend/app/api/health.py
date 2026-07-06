from fastapi import APIRouter 

router=APIRouter()

@router.get("/")
def health_check():
    return{"message":"AI Resume and Career Copilot API is running"}