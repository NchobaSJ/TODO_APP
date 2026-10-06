from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.api import auth, tasks, categories
from app.core.database import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(title="Todo API", lifespan=lifespan)

app.include_router(auth.router, prefix="/auth")
app.include_router(tasks.router)
app.include_router(categories.router)

@app.get("/")
async def root():
    return {"message": "Todo API is running"}