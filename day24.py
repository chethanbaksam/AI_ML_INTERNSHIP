from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    name: str
    email: str
    age: int


@app.post("/register")
def register_user(user: User):
    return {
        "message": "User registered successfully",
        "user": user
    }