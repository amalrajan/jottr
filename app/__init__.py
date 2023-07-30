from datetime import timedelta

from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy and migration extension
db = SQLAlchemy()
migrate = Migrate()

# Initialize JWTManager
jwt = JWTManager()


def create_app():
    app = Flask(__name__)

    # Replace with your own secret key
    app.config["SECRET_KEY"] = "your_secret_key"

    # PostgreSQL configuration
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "postgresql://postgres:root@localhost:5432/mydb"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    migrate.init_app(app, db)

    # Configure JWT settings
    app.config["JWT_SECRET_KEY"] = "your_jwt_secret_key"
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(
        hours=1
    )  # Token expiration time (optional)

    jwt.init_app(app)  # Initialize JWTManager

    # Register the blueprints
    from app.routes.auth_routes import auth_bp
    from app.routes.notes_routes import note_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(note_bp)

    with app.app_context():
        db.create_all()

    return app
