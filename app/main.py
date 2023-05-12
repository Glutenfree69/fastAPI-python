from fastapi import Body, FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import post, user, auth
from .config import settings


#models.Base.metadata.create_all(bind = engine)          #crée toutes les tables définies dans models si elle n'existe pas deja 
#on a plus besoin de la ligne du dessus vu qu'on utilise alembic pour gerer la base de donnée


# setup l'instance
app = FastAPI() 

#origins = ["https://www.google.com", "https://www.youtube.com"]        #permettre aux mecs de google et youtube de communiquer avec notre API
origins = ["*"]                                                         #tout le monde peut communiquer avec moi yes trop cool

#un middleware est un logiciel qui sert d'interface entre différentes applications ou systèmes, en leur fournissant des services communs pour faciliter leur interopérabilité
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
         
app.include_router(post.router)         #ca va aller check dans les routers et check si y a un match avec la requete
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "Yo la team fffffffoigrpognlrz"}



