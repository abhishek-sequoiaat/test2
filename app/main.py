from fastapi import FastAPI
from app.routes import users

app = FastAPI()

app.include_router(users.router)


@app.get("/")
def home():
    return {"message": "CRUD operation in FastAPI with PostgreSQL"}
