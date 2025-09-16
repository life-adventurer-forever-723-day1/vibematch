from fastapi import FastAPI, UploadFile, File, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel, Session, create_engine, select
from . import models, crud, auth, schemas, utils
import os

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["http://localhost:5173"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

DB_URL = os.getenv("DATABASE_URL", "sqlite:///./database.db")
engine = create_engine(DB_URL, connect_args={"check_same_thread": False})

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

@app.post('/signup', response_model=schemas.UserRead)
def signup(data: schemas.UserCreate):
    with Session(engine) as session:
        if crud.get_user_by_email(session, data.email):
            raise HTTPException(400, "Email already registered")
        user = crud.create_user(session, data)
        return user

@app.post('/login', response_model=schemas.Token)
def login(data: schemas.UserLogin):
    user = crud.authenticate_user(engine, data.email, data.password)
    if not user:
        raise HTTPException(401, 'Invalid credentials')
    token = auth.create_access_token({'sub': str(user.id)})
    return {'access_token': token, 'token_type': 'bearer'}

@app.get('/topics')
def list_topics():
    with Session(engine) as s:
        return s.exec(select(models.Topic)).all()

@app.post('/topics', response_model=schemas.TopicRead)
def create_topic(t: schemas.TopicCreate, user=Depends(auth.get_current_user)):
    with Session(engine) as s:
        return crud.create_topic(s, t, user.id)

@app.post('/topics/{topic_id}/answers')
def post_answer(topic_id: int, a: schemas.AnswerCreate, user=Depends(auth.get_current_user)):
    with Session(engine) as s:
        return crud.create_answer(s, topic_id, a, user.id)

@app.post('/poke/{to_user_id}')
def poke(to_user_id: int, user=Depends(auth.get_current_user)):
    with Session(engine) as s:
        return crud.poke_user(s, user.id, to_user_id)

@app.post('/messages/{to_user_id}')
def send_message(to_user_id: int, msg: schemas.MessageCreate, user=Depends(auth.get_current_user)):
    with Session(engine) as s:
        return crud.send_message(s, user.id, to_user_id, msg)

@app.post('/upload_face')
async def upload_face(file: UploadFile = File(...), user=Depends(auth.get_current_user)):
    path = await utils.save_upload(file)
    if not utils.contains_face(path):
        raise HTTPException(400, 'No face detected in image')
    with Session(engine) as s:
        u = s.get(models.User, user.id)
        u.face_photo = path
        u.verified = True
        s.add(u); s.commit()
    return {'path': path}

@app.get('/interactions')
def interactions(user=Depends(auth.get_current_user)):
    with Session(engine) as s:
        return crud.get_interactions(s, user.id)
