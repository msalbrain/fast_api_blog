from fastapi import HTTPException, status, Depends,APIRouter,Form,UploadFile,File,Response

from pymongo import MongoClient

from sqlalchemy import func
from sqlalchemy.orm import Session


from ..dependencies import get_db,get_current_user
from .. import models
from .. import schemas

from datetime import datetime
from uuid import uuid4
import os
import shutil



router = APIRouter(
    prefix='/post',
    tags=["POSTS"]
)

client = MongoClient("localhost",27017)

db = client["tryin_sth"]
collection = db["posts_sql"]
coll = db["posts_comp"]

def add_data_mini(d):
    collection.insert_one(d)

def add_data_main(d):
    coll.insert_one(d)




@router.get("/index")  #response_model=schemas.PostRead)
async def read_root(db: Session = Depends(get_db)):

    all_post = db.query(models.Post).all()

    # votes = db.query(models.Post,func.count(models.Vote.post_id).label("votes")).join(models.Vote,models.Vote.post_id == models.Post.id).group_by(models.Post.id).all()


    return {"post": all_post}

@router.get("/{id}") #response_model=schemas.PostLikeRead)
async def get_post(id: int,db: Session = Depends(get_db)):
    # query = db.query(models.Post).where(models.Post.id == id).first()

    votes = db.query(models.Post,func.count(models.Vote.post_id).label("votes")).join(models.Vote,models.Vote.post_id == models.Post.id).group_by(models.Post.id).where(models.Post.id == id).first()
    if not votes:
        query = db.query(models.Post).where(models.Post.id == id).first()

        return {"Post":query,"Votes": 0}

    return votes

@router.post("/create",response_model=schemas.PostBase)
async def create_post(title: str = Form(...),
                      mini_detail: str = Form(...),main_detail: str = Form(...),
                      image: UploadFile =File(...) ,db: Session = Depends(get_db)
                      ,user_id: int = Depends(get_current_user)
                      ):

    #
    # if not user.first():
    #     return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="invalid user")
    print(main_detail)
    image_id = uuid4()
    ext_name = os.path.splitext(image.filename)[1]
    file_name = f"{image_id}{ext_name}"

    with open(f"statics/image/{file_name}", "wb+") as buffer:
        shutil.copyfileobj(image.file, buffer)


    new_post = models.Post(title = title, mini_detail = mini_detail, main_detail = main_detail,
                           created_date =str(datetime.utcnow()),views = 0,
                           image_name = file_name,updated = "False",owner_id = user_id)


    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    print(new_post.title)
    add_data_mini({"_id": (new_post.id + 30),
                   "title": new_post.title,
                   "mini_detail": new_post.mini_detail,
                   "date_created": new_post.created_date,
                   "views": new_post.views,
                   "image": file_name,
                   "updated": new_post.updated })

    add_data_main({"_id": (new_post.id + 30),
                   "title": new_post.title,
                   "detail" : new_post.main_detail})

    return new_post

@router.delete("/{id}")
async def delete_post(id: int,db: Session = Depends(get_db)):

    query = db.query(models.Post).where(models.Post.id == id)

    if not query.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"the post with id {id} not found")

    query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

# @put("/id")
# async def update_post(id: int,db: Session = Depends(get_db)):
#
#     query = db.query(models.Post).where(models.Post.id == id)
#
#     if not query.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"the post with id {id} not found")
#

