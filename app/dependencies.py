from fastapi import Depends, HTTPException, status
from jose import JWTError,jwt
#from sqlmodel import Session
from fastapi.security import OAuth2PasswordBearer

from .models import User
from .database import SessionLocal
from .utils import SECRET_KEY,ALGORITHM
from sqlalchemy.orm import Session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")


# def get_session():
#     with Session(engine) as session:
#         yield session
#

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_user_id(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token,
                             SECRET_KEY,
                             algorithms=[ALGORITHM],
                             )

        user_id = payload.get("sub")
        print(user_id)
        if user_id is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    return int(user_id)


def get_current_user(user_id: int = Depends(get_user_id),db: Session = Depends(get_db)):

    user = db.query(User).where(User.id == user_id).first()


    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="user not authenticated")


    return user.id