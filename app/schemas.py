from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime, date


#/////////////////////////////////////////////   Users    \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


class UserCreate(BaseModel): # ce que l'user envoie a la db
    username: str
    password: str
    email: EmailStr
    adresse: str
    phone_number: str

class UserUpdate(BaseModel):
    username: str
    email: EmailStr
    adresse: str
    phone_number: str
    class Config:
        orm_mode = True

class UserOut(BaseModel): #ce que l'user recoit de la db
    id : int
    email : EmailStr
    adresse : str
    created_at : datetime
    phone_number: Optional[str] = None
    username: str
    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
    id: int

class TokenData(BaseModel):
    id: Optional[str] = None


#/////////////////////////////////////////////   Products    \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


#Juste pour visualiser tout ce qui est presént, on utilise pas cette classe dans le main:
class Product(BaseModel):
    name: str
    price: int
    image: str #Path pour le chemin vers l'image (HttpUrl si on veut acceder à l'img via un url)
    description: str
    inventory: int
    #les deux trucs du dessous ne doivent pas pouvoir être modifier par l'user cest pour ca que on les prend pas en compte ensuite
    public: bool = False 
    created_at: datetime
    

class ProductBase(BaseModel):
    name: str
    price: int
    image: str #Path #le chemin vers l'image (HttpUrl si on veut acceder à l'img via un url)
    description: str
    inventory: int

#ce qu'on utilise dans le main (extension du truc au dessus)
class ProductCreate(ProductBase):
    pass

#on aura tout les trucs présents dans ProductBase aswell
class ProductResponse(ProductBase): 
    id: int
    created_at: datetime
    user_id: int
    user: UserOut

    class Config:           # les données renvoyés sont traités en tant qu'objets
        orm_mode = True




