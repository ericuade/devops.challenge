from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class User(BaseModel):
    id: int
    name: str
    surname: str
    Linkedin: str
    age: int


def search_user(id: int):
    users = filter(lambda users: users.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error":"Usuario no encontrado, por favor ingreselo"}



users_list = [User(id=1,name="Eric", surname="Ogieglo", Linkedin="https://www.linkedin.com/in/eogieglo/", age=34),
 User(id=2,name="Eric", surname="Ogieglo", Linkedin="https://www.linkedin.com/in/eogieglo/", age=34),
 User(id=3,name="Eric", surname="Ogieglo", Linkedin="https://www.linkedin.com/in/eogieglo/", age=34)]


@app.get("/users")
async def users():
    return {"name": "Eric", "surname":"Ogieglo", "Linkedin": "https://www.linkedin.com/in/eogieglo/", "age": 34 }


@app.get("/userclass")
async def userclass():
    return User(name="Eric", surname="Ogieglo", Linkedin="https://www.linkedin.com/in/eogieglo/", age=34)


@app.get("/userslist")
async def users():
    return users_list


# Path
@app.get("/user/{id}")
async def user(id: int):
    return search_user(id)


# Query
@app.get("/user/")
async def user(id: int):
   return search_user(id)


# Añadir usuario / POST
@app.post("/user/")
async def user(user: User):
    if type(search_user(user.id)) == User:
        return {"error":"El usuario ya existe"}
    else:
        users_list.append(user)






