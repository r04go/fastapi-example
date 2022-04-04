from fastapi import FastAPI
from routes.user import user

app = FastAPI(title='Curso de FastAPI', description="Ejemplo del curso", version="3.4", openapi_tags=[{ 'name':'Vistas de Usuario', 'description':'En esta sección obtenemos la lista de usuarios' },{'name':'Acciones de Usuario', 'description':'En esta seccion podemos hacer acciones sobre los usuarios'}])
app.include_router(user)
