from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2                     # il existe la version 3 mais c'est une putin de giga merde
from psycopg2.extras import RealDictCursor
import time
from .config import settings

#Tout dans la doc de fastAPI : SQL (Relational) Databases
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'            #'postgresql://<username>:<password>@<ip-address/hostname>/<database_name>'

engine = create_engine(SQLALCHEMY_DATABASE_URL)             #objet qui sert de point d'entré à la db

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 

Base = declarative_base()

#Dependency : permet de créer une connection, effectuer des trucs, ensuite close la connexion
def get_db():
    db = SessionLocal()
    try : 
        yield db
    finally:
        db.close()


#connection to the db, on l'utilise pas mais juste pour voir comment ca marche (on utilise SQLalchemy)
# while True:

#     try:
#         conn = psycopg2.connect(host="localhost", dbname="restapi", user="postgres", password="&!ÀÇ", cursor_factory=RealDictCursor)
#         cursor = conn.cursor()                   #le cursor permet d'executer des requetes SQL quand il est combiné avec fetchall() ou execute()
#         print("Database connection was succesfull !")
#         break
#     except Exception as error:
#         print("Connection to database failed !")
#         print("error: ", error)
#         time.sleep(2)