from fastapi import APIRouter, Response, status
from config.database import cdb
from models.users import tablaUsuarios
from schemas.users_schemas import User
from cryptography.fernet import Fernet
from starlette.status import HTTP_204_NO_CONTENT

key = Fernet.generate_key()
f = Fernet(key)
user = APIRouter()

@user.get("/users", tags=['Vistas de Usuario'], response_model=list[User])
def ver_usuarios():
    return cdb.execute(tablaUsuarios.select()).fetchall()

@user.get('/users/{id}', tags=['Vistas de Usuario'], response_model=User)
def ver_un_usuario(id:str):
    return cdb.execute(tablaUsuarios.select().where(tablaUsuarios.c.id == id)).first()

@user.delete('/users/{id}', tags=['Acciones de Usuario'], status_code=status.HTTP_204_NO_CONTENT)
def borrar_usuario(id: str):
    cdb.execute(tablaUsuarios.delete().where(tablaUsuarios.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)

@user.post('/post', tags=['Acciones de Usuario'], response_model=User)
def inserta_usuario(user: User):
    new = {'nombre': user.nombre, 'email': user.email}
    new['passwd'] = f.encrypt(user.passwd.encode('utf-8'))
    result = cdb.execute(tablaUsuarios.insert().values(new))
    return cdb.execute(tablaUsuarios.select().where(tablaUsuarios.c.id == result.lastrowid)).first()

@user.put('/update', tags=['Acciones de Usuario'], response_model=User)
def actualiza_usuario(id: str, user: User):
    cdb.execute(tablaUsuarios.update().values(nombre=user.nombre, email=user.email, passwd=f.encrypt(user.passwd.encode('utf-8'))).where(tablaUsuarios.c.id==id))
    return cdb.execute(tablaUsuarios.select().where(tablaUsuarios.c.id == id)).first()
