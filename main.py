from fastapi import FastAPI, UploadFile, File, HTTPException, Depends
from database.database import get_db, Base, db_engine

app = FastAPI()

Base.metadata.create_all(bind=db_engine)

ALLOWED_TYPES = {"text/markdown", "text/plain"}
MAX_SIZE = 5*1024*1024

def validate_file(file: UploadFile):

    if not file.filename.endswith(".md"):
        raise HTTPException(400, "Invalid file format! upload only markdown")

    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(400, f"Invalid content type: {file.content_type}")


@app.post("/upload/")
async def upload_file(file: UploadFile = File(...), db = Depends(get_db)):
    validate_file(file)

    contents = await file.read()

    return {
        "content" : contents.decode("utf-8")
    }