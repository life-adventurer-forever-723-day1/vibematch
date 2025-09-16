from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserRead(BaseModel):
    id: int
    name: str
    email: str
    bio: Optional[str] = None
    interests: Optional[str] = None
    verified: bool

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TopicCreate(BaseModel):
    title: str
    description: Optional[str] = None

class TopicRead(TopicCreate):
    id: int

class AnswerCreate(BaseModel):
    text: str

class MessageCreate(BaseModel):
    text: str
