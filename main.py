from uuid import UUID
import markdown
from fastapi import FastAPI, UploadFile, File, HTTPException, Depends
from database.database import get_db, Base, db_engine
from models.NoteData import MarkdownNote
import language_tool_python
from utilities.text_cleaner import strip_markdown

app = FastAPI()

Base.metadata.create_all(bind=db_engine)

ALLOWED_TYPES = {"text/markdown", "text/plain"}
MAX_SIZE = 5*1024*1024

def validate_file(file: UploadFile):

    if not file.filename.endswith(".md"):
        raise HTTPException(400, "Invalid file format! upload only markdown")

    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(400, f"Invalid content type: {file.content_type}")


@app.post("/save")
async def upload_file(file: UploadFile = File(...), db = Depends(get_db)):
    validate_file(file)

    contents = await file.read()
    file_name = file.filename

    new_note = MarkdownNote(file_name = file_name, content = contents)
     
    db.add(new_note)
    db.commit()
    db.refresh(new_note)

    return {
        "content" : contents.decode("utf-8"),
        "file_name": file_name
    }


@app.get("/all_notes")
def get_all_notes(db = Depends(get_db)):
	notes = db.query(MarkdownNote).all()
	return notes


@app.get("/note/{id}")
def get_note(id: str, db = Depends(get_db)):

	try:
		uuid_id = UUID(id)
	except ValueError:
		raise HTTPException(status_code=400, detail="Invalid id format")
	
	note = db.query(MarkdownNote).filter(MarkdownNote.id == uuid_id).first()
	return note


@app.get("/get_markdown/{id}")
def get_markdown(id: str, db = Depends(get_db)):
	try:
		uuid_id = UUID(id)
	except ValueError:
		raise HTTPException(status_code=400, detail="Invalid id format!!")

	note = db.query(MarkdownNote).filter(MarkdownNote.id == uuid_id).first()

	html_markdown_note = markdown.markdown(note.content)

	return html_markdown_note


@app.post("/check_grammar")
async def check_grammer(file: UploadFile = File(...)):
	validate_file(file=file)

	content = await file.read()

	formatted_content = strip_markdown(content.decode("utf-8"))

	with language_tool_python.LanguageTool("en-US") as tool:
		matches = tool.check(formatted_content)

	return {
		"matches": matches
	}