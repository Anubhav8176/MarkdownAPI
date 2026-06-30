# MarkdownAPI

A backend REST API for uploading, storing, retrieving, rendering, and grammar-checking Markdown notes — built with **FastAPI**, **SQLAlchemy**, and **Python-Markdown**.

This project is built by following the [Markdown Note-Taking App](https://roadmap.sh/projects/markdown-note-taking-app) project idea from [roadmap.sh](https://roadmap.sh).

## About

MarkdownAPI lets users upload `.md` files, persist them to a database, fetch them back as raw content or rendered HTML, list all saved notes, and run a grammar check on the note content. It's a small, focused FastAPI service that demonstrates file upload handling, validation, database persistence with SQLAlchemy, Markdown-to-HTML conversion, and integration with a third-party grammar-checking tool.

## Features

- **Upload Markdown notes** — accepts `.md` files and stores their content in a database.
- **File validation** — restricts uploads to `.md` files with an allowed content type (`text/markdown` or `text/plain`), and enforces a max file size.
- **List all notes** — retrieve every saved note.
- **Fetch a note by ID** — look up a single note using its UUID.
- **Render Markdown as HTML** — convert a stored note's Markdown content into HTML on demand.
- **Grammar checking** — strip Markdown syntax from a note and run it through `language_tool_python` to surface grammar/spelling issues.

## Tech Stack

- **[FastAPI](https://fastapi.tiangolo.com/)** — web framework for building the API
- **[SQLAlchemy](https://www.sqlalchemy.org/)** — ORM / database layer
- **[Python-Markdown](https://python-markdown.github.io/)** — Markdown-to-HTML rendering
- **[language_tool_python](https://github.com/jxmorris12/language_tool_python)** — grammar and style checking
- **Python** (100%)

## Project Structure

```
MarkdownAPI/
├── core/            # Core application logic/configuration
├── database/         # Database connection/session setup
├── models/            # SQLAlchemy models (e.g. MarkdownNote)
├── utilities/        # Helper utilities (e.g. Markdown stripping for grammar checks)
├── main.py           # FastAPI app and route definitions
└── test_main.http    # HTTP requests for manually testing the API endpoints
```

## API Endpoints

| Method | Endpoint               | Description                                              |
|--------|-------------------------|------------------------------------------------------------|
| POST   | `/save`                 | Upload a `.md` file and save it as a note                  |
| GET    | `/all_notes`             | Retrieve all saved notes                                    |
| GET    | `/note/{id}`             | Retrieve a single note by its UUID                          |
| GET    | `/get_markdown/{id}`     | Retrieve a note's content rendered as HTML                  |
| POST   | `/check_grammar`         | Upload a `.md` file and run a grammar check on its content   |

### Upload validation rules

- File must have a `.md` extension.
- Content type must be `text/markdown` or `text/plain`.
- Maximum file size: 5 MB.

## Getting Started

### Prerequisites

- Python 3.9+
- Java (required by `language_tool_python` to run LanguageTool locally)

### Installation

```bash
git clone https://github.com/Anubhav8176/MarkdownAPI.git
cd MarkdownAPI

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # on Windows: venv\Scripts\activate

# Install dependencies
pip install fastapi uvicorn sqlalchemy markdown language_tool_python python-multipart
```

### Running the API

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`, with interactive docs at `http://127.0.0.1:8000/docs`.

### Testing the endpoints

A `test_main.http` file is included in the repo with sample requests you can run directly (e.g. via the JetBrains HTTP Client or the VS Code REST Client extension).

## Example Usage

**Upload a note:**

```bash
curl -X POST "http://127.0.0.1:8000/save" \
  -F "file=@notes.md;type=text/markdown"
```

**Get all notes:**

```bash
curl "http://127.0.0.1:8000/all_notes"
```

**Render a note as HTML:**

```bash
curl "http://127.0.0.1:8000/get_markdown/{note_id}"
```

**Check grammar in a note:**

```bash
curl -X POST "http://127.0.0.1:8000/check_grammar" \
  -F "file=@notes.md;type=text/markdown"
```

## Acknowledgements

This project was built as part of the [Markdown Note-Taking App](https://roadmap.sh/projects/markdown-note-taking-app) backend project series on [roadmap.sh](https://roadmap.sh/).

## Author

**Anubhav8176** — [GitHub Profile](https://github.com/Anubhav8176)

## License

No license has been specified for this project yet.
