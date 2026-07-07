from fastapi import FastAPI
from app.api.health import router 
from app.core.config import APP_NAME,APP_VERSION
app = FastAPI(title=APP_NAME,
    version=APP_VERSION
)
    

app.include_router(router)
