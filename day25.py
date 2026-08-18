from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

notes_db = []


class Note(BaseModel):
    id: int
    title: str
    content: str


@app.post("/notes/")
def add_note(note: Note):
    notes_db.append(note)
    return note


@app.get("/notes/")
def get_notes(title: str | None = None):
    if title:
        return [note for note in notes_db if title.lower() in note.title.lower()]
    return notes_db


@app.put("/notes/{note_id}")
def update_note(note_id: int, updated_note: Note):
    for index, note in enumerate(notes_db):
        if note.id == note_id:
            notes_db[index] = updated_note
            return updated_note

    raise HTTPException(status_code=404, detail="Note not found")


@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    for index, note in enumerate(notes_db):
        if note.id == note_id:
            deleted_note = notes_db.pop(index)
            return deleted_note

    raise HTTPException(status_code=404, detail="Note not found")