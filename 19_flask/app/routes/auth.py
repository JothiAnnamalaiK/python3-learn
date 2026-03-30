from flask import Blueprint
from app.controllers.auth_controller import login, verify_login, logout

auth = Blueprint("auth", __name__)

auth.add_url_rule("/login", view_func=login, methods=["GET"])
auth.add_url_rule("/verify_login", view_func=verify_login, methods=["POST"])
auth.add_url_rule("/logout", view_func=logout, methods=["GET"])
