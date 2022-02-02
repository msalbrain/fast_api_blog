#this is the sqlmodel part
# from sqlmodel import create_engine, SQLModel, Session
# import os
# from .schemas import Post, User
#
# connect_args = {
#     "check_same_thread": False
# }
# BASE_DIR = os.path.dirname(os.path.realpath(__file__))
# conn_str = "sqlite:///"+os.path.join(BASE_DIR,"app.db")
#
# engine = create_engine(conn_str, echo=False, connect_args=connect_args)
#
#
#
# def create_db_and_tables():
#     SQLModel.metadata.create_all(engine)
#

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

conn_str = "sqlite:///"+os.path.join(BASE_DIR,"apps.db")

SQLALCHEMY_DATABASE_URL = conn_str

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,echo=True,connect_args={'check_same_thread': False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


