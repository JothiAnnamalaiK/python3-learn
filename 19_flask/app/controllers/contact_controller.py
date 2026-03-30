from flask import render_template, request, flash, redirect, url_for, g
from app.services.contact_service import save_contact
from app.utils.validators import validate_contact
from app import csrf


# GET route to show contact form
def contact():
    return render_template(
        "pages/contact.html",
        errors={},  # default empty dict
        form_data={},  # default empty dict
        active_page=request.endpoint,
    )


# POST route to handle form submission
def add_contact():
    if request.method == "POST":
        # req.args.get() for query params, request.form.get() for form data
        # name = request.form.get("name")
        # email = request.form.get("email")
        # subject = request.form.get("subject")
        # message = request.form.get("message")
        # form_data = request.form.to_dict()

        form_data = g.cleaned_form  # already stripped of CSRF token by middleware
        form_data.pop("csrf_token", None)  # remove CSRF token before validation
        errors = validate_contact(form_data)

        if errors:
            flash("Please fix the errors below!", "danger")  # generic message
            return render_template(
                "pages/contact.html", errors=errors, form_data=form_data
            )

        # Call service layer
        save_contact(form_data)
        flash("Thank you! Your message has been sent.", "success")
        return redirect(url_for("main.contact"))
