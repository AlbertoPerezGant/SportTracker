from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Sports Tracker API")

app.include_router(router)
