from fastapi import HTTPException, status, Depends,APIRouter,Form


from ..dependencies import get_db,get_current_user
from sqlalchemy.orm import Session
from .. import schemas,models


router = APIRouter(
    prefix='/vote',
    tags=["Vote"]
)



@router.post("/up")
async def poster(vote: schemas.vote,db: Session = Depends(get_db),user_id: int = Depends(get_current_user)):

    post_ex = db.query(models.Post).where(models.Post.id == vote.post_id).first()

    if not post_ex:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id {vote.post_id}")

    if vote.dir == 1:
        if db.query(models.Vote).where(models.Vote.post_id == vote.post_id,models.Vote.user_id == user_id).first():
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=f"post with id {vote.post_id} as been liked by user {user_id}")

        vote = models.Vote(post_id=vote.post_id,user_id=user_id)
        db.add(vote)
        db.commit()
        return {"msg":"successfully liked post"}
    else:
        query = db.query(models.Vote).where(models.Vote.post_id == vote.post_id,models.Vote.user_id == user_id)
        if not query.first():
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=f"post with id {vote.post_id} as not been liked by user {user_id}")

        query.delete(synchronize_session=False)

        return {"msg":"successfully unliked post"}

@router.get("/total")
async def no_of_votes(post_id: int,db: Session = Depends(get_db)):
    query = db.query(models.Vote).where(models.Vote.post_id == post_id).count()

    print(query)

    return {"msg":"success"}





