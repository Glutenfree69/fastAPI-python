from app import oauth2
from .. import models, schemas, utils, oauth2
from fastapi import Body, FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from ..database import engine, get_db
from typing import List, Optional

router = APIRouter(             #permet de recup le app créer dans le main pour l'instance fastAPI // on utilise "router" et non "app" vu qu'on est plus dans le main et qu'on a importé le truc avec le nom router
    prefix="/posts",             #http requete à l'adresse /posts pour tout les trucs pour eviter de le réecrire à chaque route  
    tags=["Products"]
)                     

@router.get("/" , response_model=List[schemas.ProductResponse])           #faut une liste car on recupere plusieurs postes ici
def get_posts(db : Session = Depends(get_db), limit: int = 100, skip: int = 0, search: Optional[str] = ""):           #par default on affiche 100 postes, on en skip 0 et on ne precise rien dans le recherche
    # cursor.execute(""" SELECT * FROM products """)
    # posts = cursor.fetchall()
    
    posts = db.query(models.Product).filter(models.Product.name.contains(search)).limit(limit).offset(skip).all()
    return posts



@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ProductResponse)
def create_posts(post: schemas.ProductCreate, db : Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):         #la dernière dependance permet d'obliger l'user à être co pour créer un truc
    # cursor.execute(""" INSERT INTO products (name, price, description, inventory, created_at, public) VALUES (%s, %s, %s, %s, %s, %s) RETURNING * """, (post.name, post.price, post.description, post.inventory, post.created_at, post.public))
    # new_post = cursor.fetchone()
    # conn.commit() #push les changements dans la db

    print(current_user.id)                   #juste pour visualiser, ca sert a rien en soit
    new_post = models.Product(user_id=current_user.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post



@router.get("/{id}", response_model=schemas.ProductResponse)
def get_post(id: int, db : Session = Depends(get_db)):
    # cursor.execute(""" SELECT * FROM products WHERE id = %s """, (str(id),)) #la virgule apres str(id) sert a rien mais j'ai des problèmes si je la met pas
    # post = cursor.fetchone()
    
    post = db.query(models.Product).filter(models.Product.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id : {id} was not found") #si on a une erreur 404, on renvoie le message
    return post



@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT) #status code 204 quand on supprime qqch, avec un 204 on ne renvoie aucune data
def delete_post(id: int, db : Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute(""" DELETE FROM products WHERE id = %s RETURNING *""", (str(id),))
    # deleted_post = cursor.fetchone()
    # conn.commit()

    post_query = db.query(models.Product).filter(models.Product.id == id)
    post = post_query.first()


    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id : {id} does not exist")
    
    if post.user_id != current_user.id:          #verifier que l'user delete un poste que lui a créer et pas le poste d'un autre boug
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail = f"Not authorized to perform requested action")

    post_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)



@router.put("/{id}", response_model=schemas.ProductResponse)
def update_post(id: int, updated_post: schemas.ProductCreate, db : Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute(""" UPDATE products SET name = %s, price = %s, description = %s, inventory = %s WHERE id = %s RETURNING * """, (post.name, post.price, post.description, post.inventory, str(id)))
    # updated_post = cursor.fetchone()
    # conn.commit()

    post_query = db.query(models.Product).filter(models.Product.id == id)
    post = post_query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id : {id} does not exist")
    
    if post.user_id != current_user.id:          #verifier que l'user update un poste que lui a créer et pas le poste d'un autre boug
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail = f"Not authorized to perform requested action")
    
    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()
    return post_query.first()