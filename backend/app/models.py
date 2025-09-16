from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
    hashed_password: str
    bio: Optional[str] = None
    interests: Optional[str] = None
    face_photo: Optional[str] = None
    verified: bool = False
    flagged: bool = False

class Topic(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: Optional[str]
    created_at: datetime = Field(default_factory=datetime.utcnow)

class Answer(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    topic_id: int
    user_id: int
    text: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

class Poke(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    from_user: int
    to_user: int
    created_at: datetime = Field(default_factory=datetime.utcnow)

class Message(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    sender_id: int
    receiver_id: int
    text: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

class Match(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user1_id: int
    user2_id: int
    status: str = 'pending'
    reveal_unlocked: bool = False
