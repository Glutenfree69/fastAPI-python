Start l'env virtuel : source venv/bin/activate      Stop : deactivate

Start localhost : uvicorn app.main:app --reload // premier app pour dire que main est dans le dossier app et le deuxieme app pour le fastAPI instance qu'on nomme dans le main
(doc fastAPI pour plus d'info)              // --reload pour que les changements soient pris en compte sans devoir restart le serveur

Difference entre un modele et un schema : 
Un modèle est une représentation abstraite d'un système ou d'un processus, 
tandis qu'un schéma est une représentation visuelle de ce modèle qui montre comment 
les différentes entités sont reliées entre elles.


Si on change / ajoute un bail dans les models on peut appliquer les changements direct a la bdd sans devoir la sup
grâce à alembic.
commande : alembic revision  --autogenerate -m "message pour dire ce qu'on fait"
ca va generer un fichier dans alembic/version avec les changements qu'on a fait
pour les appliquer : alembic upgrade head

Pour installer toute les dépendances après avoir cloner notre bail voici la commande : 
pip install -r requirements.txt

Pour retrouver l'url du site :       https://fastapi-dylan.herokuapp.com/
heroku apps:info fastapi-dylan

commande heroku : 
se log : heroku login
faire une action sur l'api : heroku run "l'action à faire"
créer les tables dans la bdd de l'instance heroku : heroku run "alembic upgrade head", 
à faire chaque fois qu'on modifie un truc avec alembic (voir au dessus pour la commande)

Pour push les changements dans notre application :
git add .
git commit -m "..."
git push origin main (pour mon github)
git push heroku main (pour que les changements soit pris en compte sur l'appli)

Pour executer une commande dans un conteneur : 
docker-compose run <service_name> <command>

Pour mettre a jour les tables de la db dans le conteneur : 
docker-compose run api alembic upgrade head

nouvelle commande vu qu'on a 2 docker-compose : 
docker-compose -f docker-compose-dev.yml up -d 

pour acceder au conteneur avec des commandes bash : 
docker exec -it restapi-api-1 bash


UML : 

Diagramme de cas d'utilisation
Diagramme de sequence (ptet)
Diagramme de Merise

Amelioration pour rncp : 

Reflechir sur l'encapsulation
Rajouter une interface de payement (moker si necessaire) afin de mettre en place un suivis des commandes, car c'est avant tout la base d'un site e commerce