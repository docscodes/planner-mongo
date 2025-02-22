import asyncio
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from database.connection import Settings
from routes.events import event_router
from routes.users import user_router

app = FastAPI()

settings = Settings()

app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")


@app.on_event("startup")
async def init_db():
  await settings.initialize_database()


@app.get("/")
async def home():
  return {"Hello": "World"}
