from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from datetime import datetime, timedelta
from .crud import get_user_by_id_wrap
import os

SECRET = os.getenv('JWT_SECRET', 'devsecret')
ALGORITHM = 'HS256'
oauth2 = OAuth2PasswordBearer(tokenUrl='login')

def create_access_token(data: dict, expires_delta: int = 60*24*7):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=expires_delta)
    to_encode.update({'exp': expire})
    return jwt.encode(to_encode, SECRET, algorithm=ALGORITHM)

def get_current_user(token: str = Depends(oauth2)):
    try:
        payload = jwt.decode(token, SECRET, algorithms=[ALGORITHM])
        user_id = int(payload.get('sub'))
    except JWTError:
        raise HTTPException(401, 'Could not validate credentials')
    user = get_user_by_id_wrap(user_id)
    if not user:
        raise HTTPException(401, 'User not found')
    return user
