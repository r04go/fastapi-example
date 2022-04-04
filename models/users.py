from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, Text, String, Date
from config.database import meta, engine

tablaUsuarios = Table('usuarios', meta, 
    Column('id', Integer, primary_key=True), 
    Column('nombre', String(255)), 
    Column('email', String(255)), 
    Column('passwd', String(255)))

meta.create_all(engine)
