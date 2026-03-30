from functools import wraps
from flask import session, redirect, url_for, request, flash


def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if "user_id" not in session:
            flash("Please login to continue", "warning")
            return redirect(url_for("auth.login", next=request.url))
        return f(*args, **kwargs)

    return wrapper
