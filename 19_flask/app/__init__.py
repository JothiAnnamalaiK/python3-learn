from flask import (
    Flask,
    render_template,
    current_app,
    session,
    redirect,
    url_for,
    request,
)
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import text
from flask_wtf import CSRFProtect
from flask_wtf.csrf import CSRFError


db = SQLAlchemy()  # define globally here
migrate = Migrate()  # global migrate instance
csrf = CSRFProtect()  # create CSRF object


def create_app():
    app = Flask(__name__)

    # CSRF Init
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
    csrf.init_app(app)  # attach CSRF protection

    # Load default config
    env = os.environ.get("FLASK_ENV", "development")
    if env == "production":
        app.config.from_object("app.config.config.ProductionConfig")
    else:
        app.config.from_object("app.config.config.DevelopmentConfig")

    # Ensure exceptions propagate to error handlers
    app.config["PROPAGATE_EXCEPTIONS"] = True

    # Initialize DB with app
    db.init_app(app)
    migrate.init_app(app, db)  # db migration

    # IMPORT models here so Flask-Migrate sees them
    from app.models.user import User
    from app.models.contact import Contact

    # check_db_connection()
    if env != "production":
        with app.app_context():
            try:
                db.session.execute(text("SELECT 1"))
                print("✅ Database connected successfully!")
            except Exception as e:
                print("❌ Database connection failed!")
                print(e)

    # Register blueprints
    from app.routes.main import main

    app.register_blueprint(main)

    from app.routes.api.api import api

    app.register_blueprint(api)
    # app.register_blueprint(auth)

    from app.routes.auth import auth

    app.register_blueprint(auth)

    # Register error pages
    from .errors import register_error_handlers

    register_error_handlers(app)

    # Make current_user available in all templates
    @app.context_processor
    def inject_user():
        return dict(current_user=session.get("user_name"))

    return app
