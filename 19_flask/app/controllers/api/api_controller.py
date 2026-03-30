from flask import request
from app import csrf

from app.services.contact_service import save_contact, get_all_contacts
from app.utils.validators import validate_contact
from app.utils.response import api_response
from app.utils.serializers import contact_to_dict


def get_contacts_api():
    contacts = get_all_contacts()

    # Convert objects to dict
    data = []
    for contact in contacts:
        data.append(
            {
                "id": contact.id,
                "name": contact.name,
                "email": contact.email,
                "subject": contact.subject,
                "message": contact.message,
                "created_at": (
                    contact.created_at.strftime("%Y-%m-%d %H:%M:%S")
                    if contact.created_at
                    else None
                ),
            }
        )

    return api_response(True, "Contacts fetched successfully", data, 200)


@csrf.exempt
def create_contact_api():
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form.to_dict()

    if not data:
        return api_response(False, "Invalid JSON data", status=400)

    errors = validate_contact(data)

    if errors:
        return api_response(False, "Validation failed", errors, 422)

    contact = save_contact(data)

    return api_response(
        True, "Contact created successfully", contact_to_dict(contact), status=201
    )
