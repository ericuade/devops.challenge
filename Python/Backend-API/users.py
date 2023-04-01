from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    surname: str
    Linkedin: str
    age: int

users_list = [User(name="Eric", surname="Ogieglo", Linkedin="https://www.linkedin.com/in/eogieglo/", age=34),
 User(name="Eric", surname="Ogieglo", Linkedin="https://www.linkedin.com/in/eogieglo/", age=34),
 User(name="Eric", surname="Ogieglo", Linkedin="https://www.linkedin.com/in/eogieglo/", age=34)]

@app.get("/users")
async def users():
    return {"name": "Eric", "surname":"Ogieglo", "Linkedin": "https://www.linkedin.com/in/eogieglo/", "age": 34 }

@app.get("/userclass")
async def userclass():
    return User(name="Eric", surname="Ogieglo", Linkedin="https://www.linkedin.com/in/eogieglo/", age=34)

@app.get("/userslist")
async def users():
    return users_list
