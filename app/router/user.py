from fastapi import HTTPException, status, Depends,APIRouter,Form
from fastapi.security import OAuth2PasswordRequestForm


from ..dependencies import get_db,get_current_user
from sqlalchemy.orm import Session
from .. import schemas,utils,models
from datetime import datetime,timedelta


router = APIRouter(
    prefix='/user',
    tags=["User"]
)








@router.post("/signup")
async def signup(Name: str=Form(...),
                 Email: str =Form(...),
                 About:str = Form(...),
                 Password:str = Form(...),
                 Telephone:str = Form(...),
                 db: Session = Depends(get_db)):

    if_user = db.query(models.User).where(models.User.name == Name).first()
    if_email = db.query(models.User).where(models.User.email == Email).first()
    if if_user:
        return {"msg":"username of email already in use"}
    if if_email:
        return {"msg":"username of email already in use"}

    new_user= models.User(name= Name,email= Email,about= About,created= str(datetime.utcnow()),password= utils.hashed_password(Password),telephone = Telephone)

    db.add(new_user)
    db.commit()

    return {"msg":"user successfully added"}


@router.post("/login/")
def login(form_data: OAuth2PasswordRequestForm = Depends(),db: Session = Depends(get_db)):
    # fetch db user by email
    user = db.query(models.User).where(models.User.email == form_data.username).first()

    if user is None:
        raise HTTPException(
            status_code=400, detail="Email does not exists!")
    # match user  password
    if not utils.verify_password(form_data.password,user.password):
        raise HTTPException(status_code=400, detail="Incorrect password!")
    # create token expiration  in minutes
    access_token_expires = timedelta(minutes=utils.ACCESS_TOKEN_EXPIRE_MINUTES)
    # create jwt token
    access_token = utils.create_jwt_token(
        {"sub": str(user.id)}, expires_delta=access_token_expires)
    return {
        "access_token": access_token,
        "token_type": "Bearer"
    }


@router.get("/me",response_model=schemas.UserRead)
def get_user(db: Session = Depends(get_db),usr_id: int = Depends(get_current_user)):

    return db.query(models.User).where(models.User.id == usr_id).first()









