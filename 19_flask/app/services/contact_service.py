from app import db
from app.models.contact import Contact


def get_all_contacts():
    return Contact.query.order_by(Contact.id.desc()).all()


def save_contact(data):
    # new_contact = Contact(name=name, email=email, subject=subject, message=message)
    new_contact = Contact(**data)

    db.session.add(new_contact)
    db.session.commit()
    return new_contact
