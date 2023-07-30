from http import HTTPStatus

from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from app.controllers.auth_controller import authenticate_user, signup_user
from app.models.response_models import ResponseModel

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["POST"])
def login_route():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    # Call the login function from the auth_controller
    result = authenticate_user(username, password)

    if result.status == HTTPStatus.OK:
        return (
            ResponseModel(
                status=HTTPStatus.OK,
                message="User authenticated",
                data={"access_token": result.data["access_token"]},
            ).to_dict(),
            200,
        )
    else:
        return (
            ResponseModel(
                status=HTTPStatus.UNAUTHORIZED,
                message="Invalid credentials",
            ).to_dict(),
            401,
        )


@auth_bp.route("/signup", methods=["POST"])
def signup_route():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    # Call the signup function from the auth_controller
    result = signup_user(username, password)

    if result.status == HTTPStatus.CREATED:
        return (
            ResponseModel(
                status=HTTPStatus.CREATED,
                message="User registered successfully",
                data={"access_token": result.data["access_token"]},
            ).to_dict(),
            201,
        )
    else:
        return (
            ResponseModel(
                status=HTTPStatus.BAD_REQUEST,
                message="Username already exists. Please choose a different username.",
            ).to_dict(),
            400,
        )


@auth_bp.route("/protected", methods=["GET"])
@jwt_required()  # This decorator will require a valid JWT token to access this route
def protected_route():
    return jsonify({"message": "You have accessed a protected route!"}), 200
