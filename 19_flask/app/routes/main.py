# TO INSTALL: pip install flask

# googleseaarch: flask minimal app

from flask import (
    Flask,
    render_template,
    request,
    Blueprint,
    redirect,
    url_for,
    flash,
    g,
)
from datetime import datetime

from app.services.contact_service import save_contact
from app.models.contact import Contact
from app.controllers.contact_controller import contact, add_contact


# app = Flask(__name__)# create a Flask app instance
main = Blueprint("main", __name__)  # create a Blueprint instance for the main routes


@main.route("/")  # define a route for the root URL
def home():
    # return "<p>Hello, from flask app!</p>"

    return render_template(
        "pages/index.html",
        user_name="Jothi",
        today=datetime.now().strftime("%Y-%m-%d"),
        active_page=request.endpoint,
    )


@main.route("/about")
def about():
    return render_template("pages/about.html", active_page=request.endpoint)


@main.route("/services")
def services():
    return render_template("pages/services.html", active_page=request.endpoint)


# contact page related routes
# GET → show form
main.add_url_rule("/contact", view_func=contact, methods=["GET"])

# POST → handle submission
main.add_url_rule("/add_contact", view_func=add_contact, methods=["POST"])


# middlewares
@main.before_app_request
def strip_csrf_token():
    """
    Remove 'csrf_token' from POST data before routes handle it.
    This avoids passing it to models accidentally.
    """
    if request.method in ("POST", "PUT", "PATCH"):
        # Convert ImmutableMultiDict to dict to modify
        data = request.form.to_dict()
        data.pop("csrf_token", None)
        # Attach cleaned data to g (global request context)
        g.cleaned_form = data
