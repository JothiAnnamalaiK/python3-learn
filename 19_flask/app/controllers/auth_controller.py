from flask import render_template, request, redirect, url_for, flash, session
from app.services.auth_service import authenticate_user, create_user
from app.utils.validators import validate_login


def login():
    # return render_template("pages/auth/login.html")
    return render_template(
        "pages/auth/login.html",
        errors={},  # default empty dict
        form_data={},  # default empty dict
    )


def verify_login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        form_data = request.form.to_dict()
        errors = validate_login(form_data)

        if errors:
            flash("Please fix the errors below!", "danger")  # generic message
            return render_template(
                "pages/auth/login.html", errors=errors, form_data=form_data
            )

        user = authenticate_user(email, password)
        print("Authenticated user:", user)  # Debugging statement

        if user:
            session["user_id"] = user.id
            session["user_name"] = user.name
            flash("Login successful!", "success")

            # redirect to previous page
            next_page = request.args.get("next")
            return redirect(next_page or url_for("main.home"))
        else:
            flash("Invalid email or password", "danger")
            return render_template(
                "pages/auth/login.html", errors=errors, form_data=form_data
            )


def logout():
    session.clear()
    flash("Logged out successfully", "success")
    return redirect(url_for("auth.login"))
