from .. import models, schemas, utils
from fastapi import Body, FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from ..database import engine, get_db

router = APIRouter(         #permet de recup le app créer dans le main pour l'instance fastAPI
    prefix="/users",
    tags=["Users"]
)            

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)         #on utilise "router" et non "app" vu qu'on est plus dans le main et qu'on a importé le truc avec le nom router
def create_user(user : schemas.UserCreate ,db : Session = Depends(get_db)):
     
    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    new_user = models.Users(**user.dict()) 
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/{id}", response_model=schemas.UserOut)
def get_user(id : int, db : Session = Depends(get_db)):
    user = db.query(models.Users).filter(models.Users.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id: {id} does not exist")
    
    return user