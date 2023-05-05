from .database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String, Boolean, func
from sqlalchemy.dialects.postgresql import BYTEA

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key = True, nullable = False)
    name = Column(String, nullable = False)
    price = Column(Integer, nullable = False)
    image = Column(String, nullable = False)
    description = Column(String, nullable = False)
    inventory = Column(Integer, nullable = False)
    public = Column(Boolean, nullable = False, server_default = 'FALSE')
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable = False)
    user = relationship("Users")                          #permet de recup les infos de l'user qui a créer le post via l'objet Product



class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True, nullable = False)
    username = Column(String, nullable = False, unique = True)
    password = Column(String, nullable = False)
    role = Column(Integer, nullable = False, server_default='0')
    email = Column(String, nullable = False, unique = True)
    adresse = Column(String, nullable = False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)
    phone_number = Column(String, nullable = False)