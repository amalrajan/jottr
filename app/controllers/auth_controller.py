from http import HTTPStatus

from flask_jwt_extended import create_access_token

from app import db
from app.models.response_models import ResponseModel
from app.models.user_model import User


def authenticate_user(username, password):
    # Authentication logic
    # Fetch the user from the database based on the provided username
    user = User.query.filter_by(username=username).first()

    if user and user.check_password(password):
        # Password matches, create and return the JWT token
        access_token = create_access_token(identity=username)
        return ResponseModel(
            status=HTTPStatus.OK,
            message="User authenticated",
            data={"access_token": access_token},
        )

    return ResponseModel(
        status=HTTPStatus.UNAUTHORIZED,
        message="Invalid credentials",
    )


def signup_user(username, password):
    # Check if the username is already taken
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return ResponseModel(
            status=HTTPStatus.BAD_REQUEST,
            message="Username already exists. Please choose a different username.",
        )

    # Create a new user and save it to the database
    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()

    # Create and return the JWT token for the newly registered user
    access_token = create_access_token(identity=username)
    return ResponseModel(
        status=HTTPStatus.CREATED,
        message="User registered successfully",
        data={"access_token": access_token},
    )
