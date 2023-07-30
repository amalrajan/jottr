from http import HTTPStatus

from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required

from app.controllers.notes_controller import (
    create_notes,
    get_user_notes,
    get_note_by_username_id,
    delete_note_by_username_id,
)
from app.models.response_models import ResponseModel

note_bp = Blueprint("note", __name__)


@note_bp.route("/notes", methods=["GET"])
@jwt_required()  # Requires a valid Bearer token for access
def get_notes():
    current_username = get_jwt_identity()
    notes = get_user_notes(current_username)

    result = [
        {"id": note.id, "title": note.title, "content": note.content} for note in notes
    ]

    return (
        ResponseModel(
            status=HTTPStatus.OK,
            message="Notes retrieved successfully",
            data=result,
        ).to_dict(),
        200,
    )


@note_bp.route("/notes", methods=["POST"])
@jwt_required()  # Requires a valid Bearer token for access
def create_note():
    # Create note with title and content
    data = request.get_json()
    title = data.get("title")
    content = data.get("content")

    new_note = create_notes(get_jwt_identity(), title, content)

    return (
        ResponseModel(
            status=HTTPStatus.CREATED,
            message="Note created successfully",
            data={
                "id": new_note.id,
                "title": new_note.title,
                "content": new_note.content,
            },
        ).to_dict(),
        201,
    )


@note_bp.route("/notes/<int:note_id>", methods=["GET"])
@jwt_required()  # Requires a valid Bearer token for access
def get_note_by_id(note_id):
    current_username = get_jwt_identity()

    # Get note by id
    note = get_note_by_username_id(current_username, note_id)

    return (
        ResponseModel(
            status=HTTPStatus.OK,
            message="Note retrieved successfully",
            data={
                "id": note.id,
                "title": note.title,
                "content": note.content,
            },
        ).to_dict(),
        200,
    )


@note_bp.route("/notes/<int:note_id>", methods=["DELETE"])
@jwt_required()  # Requires a valid Bearer token for access
def delete_note_by_id(note_id):
    current_username = get_jwt_identity()

    # Delete note by id
    note = delete_note_by_username_id(current_username, note_id)

    if note is None:
        return (
            ResponseModel(
                status=HTTPStatus.NOT_FOUND,
                message="Note not found",
            ).to_dict(),
            404,
        )

    return (
        ResponseModel(
            status=HTTPStatus.OK,
            message="Note deleted successfully",
        ).to_dict(),
        200,
    )
