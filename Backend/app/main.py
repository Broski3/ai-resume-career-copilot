from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def healt_check():
    return{"message":"AI resume and career copilot API is running!!"}