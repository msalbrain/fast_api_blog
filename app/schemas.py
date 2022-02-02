# from typing import List, Optional
#
# from sqlmodel import SQLModel, Field,Relationship
#
# from datetime import datetime
#
#
#
# class UserBase(SQLModel):
#     name: str
#     email: str
#
# class User(UserBase,table=True):
#     id: Optional[int] = Field(None,primary_key=True)
#     created: datetime = Field(default=datetime.utcnow())
#     posts: List["Post"] = Relationship(back_populates="user")
#     password: str
#
# class UserCreate(UserBase):
#     password: str
#
#
#
# # user
#
# class UserRead(UserBase):
#     id: Optional[int] = Field(None, primary_key=True)
#     created_at: datetime
#
#
# # user schema for update
#
# class UserUpdate(SQLModel):
#     name: Optional[str] = None
#     email: Optional[str] = None
#
#
# # user schema for login input
#
#
# class PostBase(SQLModel):
#     title: str
#     mini_detail: Optional[str]
#     main_detail: str
#
#
#
# class Post(PostBase,table=True):
#     id: Optional[int] = Field(default=None,primary_key=True)
#     image_name: Optional[str]
#     created: datetime = Field(default=datetime.utcnow())
#     user: Optional[User] = Relationship(back_populates="post")
#     user_id: Optional[int] = Field(default=None, foreign_key="user.id")
#     updated: bool
#     views: int
#     likes: int
#
# class PostCreate(PostBase):
#     image_name: str
#
# class PostRead(PostBase):
#     id: int
#     image_name: str
#     created: datetime
#     user_id: int
#     updated: bool
#     views: int
#     likes: Optional[int]
#
# class UserWithPost(UserRead):
#     post: List[PostRead] = []
#
#
# class PostWithUser(PostRead):
#     user: UserRead
#
# class UserVideoLikesLink(SQLModel, table=True):
#     user_id: Optional[int] = Field(None, primary_key=True, foreign_key="user.id")
#     post_id: Optional[int] = Field(None, primary_key=True, foreign_key="post.id")

from pydantic import BaseModel,EmailStr
from pydantic.types import conint
from typing import Optional,List

class UserBase(BaseModel):
    email: EmailStr
    password: str

class User(BaseModel):
    name: str
    about: Optional[str] = ""
    created: str
    telephone: str

class UserRead(BaseModel):
    id: int
    name: str
    about: Optional[str] = ""
    created: str

    class Config:
        orm_mode = True

class PostBase(BaseModel):
    id: int
    title: str
    mini_detail: str
    main_detail: str
    owner: UserRead

    class Config:
        orm_mode = True


class PostRead(BaseModel):
    post: List[PostBase]

class PostLikeRead(BaseModel):
    Post: PostBase
    votes: int

class vote(BaseModel):
    post_id: int
    dir: conint(le=1)



