from .database import Base
from sqlalchemy import Column, String, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship




class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    mini_detail = Column(Text, nullable=False)
    main_detail = Column(Text, nullable=False)
    updated = Column(Text, nullable=False)
    created_date = Column(String, nullable=False)
    views = Column(Integer,nullable=False)
    image_name = Column(String)
    owner_id = Column(Integer,ForeignKey("user.id",
                        ondelete="CASCADE"),nullable=False)
    owner = relationship("User")


class User(Base):
    __tablename__ = "user"

    id = Column(Integer,primary_key=True, nullable=False)
    name = Column(String,nullable=False)
    email = Column(String,nullable=False)
    about = Column(String,nullable=False)
    created = Column(String,nullable=False)
    password = Column(String,nullable=False)
    telephone = Column(String,nullable=False)


class Vote(Base):
    __tablename__ = "vote"

    user_id = Column(Integer,ForeignKey("user.id",ondelete="CASCADE"),primary_key=True)
    post_id = Column(Integer,ForeignKey("post.id",ondelete="CASCADE"),primary_key=True)