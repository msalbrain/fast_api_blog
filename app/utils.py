from passlib.context import CryptContext
from jose import jwt

from typing import Optional
from datetime import datetime,timedelta

SECRET_KEY = "I should really change this later"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 15

password_context = CryptContext(schemes=["bcrypt"],deprecated="auto")

def hashed_password(plain_password):
    return password_context.hash(plain_password)


def verify_password(plain_pass,hashed_pass):
    return password_context.verify(plain_pass,hashed_pass)


# create new jwt token from user_id
def create_jwt_token(payload: dict, expires_delta: Optional[timedelta] = None):
    encoded_payload = payload.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    encoded_payload.update({"exp": expire})
    encoded_jwt = jwt.encode(encoded_payload, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# decode jwt token
def decode_jwt_token(token):
    return jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)











