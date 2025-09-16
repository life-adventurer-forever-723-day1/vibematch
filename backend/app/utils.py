import os
from fastapi import UploadFile
from pathlib import Path
from PIL import Image
import cv2

UPLOAD_DIR = Path(__file__).parent / 'uploads'
UPLOAD_DIR.mkdir(exist_ok=True)

async def save_upload(file: UploadFile) -> str:
    ext = file.filename.split('.')[-1]
    path = UPLOAD_DIR / f"{file.filename}"
    contents = await file.read()
    with open(path, 'wb') as f: f.write(contents)
    return str(path)

cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def contains_face(filepath: str) -> bool:
    img = cv2.imread(filepath)
    if img is None: return False
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray, 1.1, 4)
    return len(faces) > 0
