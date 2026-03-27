from app import db
from app.models.contact import Contact


def validate_contact(data):
    errors = {}
    if not data.get("name"):
        errors["name"] = "Name is required"
    if not data.get("email"):
        errors["email"] = "Email is required"
    elif Contact.query.filter_by(email=data["email"]).first():
        errors["email"] = "Email already used to send a message"

    if not data.get("subject"):
        errors["subject"] = "Subject is required"
    if not data.get("message"):
        errors["message"] = "Message is required"
    return errors


def save_contact(data):
    # new_contact = Contact(name=name, email=email, subject=subject, message=message)
    new_contact = Contact(**data)

    db.session.add(new_contact)
    db.session.commit()
    return new_contact
