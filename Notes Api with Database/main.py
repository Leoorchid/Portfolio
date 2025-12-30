from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
import requests
from typing import Optional

app = FastAPI()

conn = sqlite3.connect("Notes.db")
cur = conn.cursor()

cur.execute(
    """

CREATE TABLE IF NOT EXISTS NotePage(
            
        noteText TEXT NOT NULL
            
            );

"""
)
conn.commit()
conn.close()


class Note(BaseModel):
    note: str
    pad: str


class Name(BaseModel):
    name: str


@app.get("/")
def root():
    return {"m": "o"}


@app.post("/postNotes")
def postNotes(note: Note):
    conn = sqlite3.connect("Notes.db")
    cur = conn.cursor()
    cur.execute(f"INSERT INTO {note.pad} (noteText) VALUES(?)", (note.note,))
    conn.commit()
    conn.close()


@app.get("/getNotes")
def getNotes(pad: str):
    conn = sqlite3.connect("Notes.db")
    cur = conn.cursor()
    cur.execute(f"SELECT noteText FROM {pad}")
    rows = cur.fetchall()
    notes = []
    for row in rows:
        print(row[0])
        notes.append(row[0])
    conn.close()
    return notes


@app.get("/getPads")
def getPads():
    conn = sqlite3.connect("Notes.db")
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = []
    for row in cur.fetchall():
        tables.append(row[0])

    return tables


@app.post("/delNote")
def delNote(note: Note):
    conn = sqlite3.connect("Notes.db")
    cur = conn.cursor()
    cur.execute(f"DELETE FROM {note.pad} WHERE noteText = ?", (note.note,))
    conn.commit()
    conn.close()


@app.post("/makePad")
def makePad(name: Name):
    conn = sqlite3.connect("Notes.db")
    cur = conn.cursor()
    cur.execute(f"CREATE TABLE IF NOT EXISTS {name.name}(noteText TEXT NOT NULL);")
    conn.commit()
    conn.close()


@app.post("/delPad")
def delPad(name: Name):
    conn = sqlite3.connect("Notes.db")
    cur = conn.cursor()
    cur.execute(f"DROP TABLE IF EXISTS {name.name};")
    conn.commit()
    conn.close()
