from app.models.notes_model import Note
from app import db


def get_user_notes(username):
    return Note.query.filter_by(username=username).all()


def get_note_by_username_id(username, note_id):
    return Note.query.filter_by(username=username, id=note_id).first()


def delete_note_by_username_id(username, note_id):
    note = Note.query.filter_by(username=username, id=note_id).first()
    db.session.delete(note)
    db.session.commit()

    return note


def create_notes(username, title, content):
    new_note = Note(
        username=username,
        title=title,
        content=content,
    )
    db.session.add(new_note)
    db.session.commit()

    return new_note
