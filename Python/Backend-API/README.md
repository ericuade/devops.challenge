# Requisitos previos

Hay requisitos previos que dependeran del entorno donde se ejecutan, por ejemplo, version de Python, pip, etc.

# Ejecutar servidor

- pipenv install fastapi
- pipenv install uvicorn
- uvicorn main:app --reload

- URL: http://localhost:8000

# Rutas

- URL: http://localhost:8000/
- URL: http://localhost:8000/users
- URL: http://localhost:8000/userclass
- URL: http://localhost:8000/userslist
- URL: http://localhost:8000/user/{id}
- URL: http://localhost:8000/user/?id=int
