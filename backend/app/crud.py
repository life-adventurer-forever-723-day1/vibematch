from sqlmodel import Session, select, create_engine
from . import models, schemas
from passlib.context import CryptContext
from typing import Optional

pwd = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user_by_email(session: Session, email: str) -> Optional[models.User]:
    stmt = select(models.User).where(models.User.email==email)
    return session.exec(stmt).first()

def get_user_by_id(session: Session, id: int) -> Optional[models.User]:
    return session.get(models.User, id)

def get_user_by_id_wrap(id: int):
    import os
    engine = create_engine(os.getenv('DATABASE_URL','sqlite:///./database.db'), connect_args={"check_same_thread": False})
    from sqlmodel import Session
    with Session(engine) as s:
        return get_user_by_id(s, id)

def create_user(session: Session, user: schemas.UserCreate):
    hashed = pwd.hash(user.password)
    u = models.User(name=user.name, email=user.email, hashed_password=hashed)
    session.add(u)
    session.commit()
    session.refresh(u)
    return u

def authenticate_user(engine, email, password):
    from sqlmodel import Session
    with Session(engine) as s:
        user = get_user_by_email(s, email)
        if not user: return None
        if not pwd.verify(password, user.hashed_password): return None
        return user

def create_topic(session: Session, t: schemas.TopicCreate, owner_id: int):
    top = models.Topic(title=t.title, description=t.description)
    session.add(top); session.commit(); session.refresh(top)
    return top

def create_answer(session: Session, topic_id: int, a: schemas.AnswerCreate, user_id: int):
    ans = models.Answer(topic_id=topic_id, user_id=user_id, text=a.text)
    session.add(ans); session.commit(); session.refresh(ans)
    return ans

def poke_user(session: Session, from_id: int, to_id: int):
    p = models.Poke(from_user=from_id, to_user=to_id)
    session.add(p); session.commit(); session.refresh(p)
    stmt = select(models.Poke).where(models.Poke.from_user==to_id, models.Poke.to_user==from_id)
    mutual = session.exec(stmt).first()
    if mutual:
        mstmt = select(models.Match).where(((models.Match.user1_id==from_id) & (models.Match.user2_id==to_id)) | ((models.Match.user1_id==to_id) & (models.Match.user2_id==from_id)))
        if not session.exec(mstmt).first():
            match = models.Match(user1_id=from_id, user2_id=to_id, status='pending')
            session.add(match); session.commit(); session.refresh(match)
            return {'mutual': True, 'match': match}
    return {'mutual': False}

def send_message(session: Session, sender_id: int, to_id: int, msg: schemas.MessageCreate):
    m = models.Message(sender_id=sender_id, receiver_id=to_id, text=msg.text)
    session.add(m); session.commit(); session.refresh(m)
    return m

def get_interactions(session: Session, user_id: int):
    stmt_a = select(models.Answer).where(models.Answer.user_id==user_id)
    stmt_p = select(models.Poke).where((models.Poke.from_user==user_id) | (models.Poke.to_user==user_id))
    stmt_m = select(models.Message).where((models.Message.sender_id==user_id) | (models.Message.receiver_id==user_id))
    return {
        'answers': session.exec(stmt_a).all(),
        'pokes': session.exec(stmt_p).all(),
        'messages': session.exec(stmt_m).all()
    }
