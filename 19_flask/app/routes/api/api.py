from app.routes.api import api
from app.controllers.api.api_controller import (
    create_contact_api,
    get_contacts_api,
)


# GET → get all contacts
api.add_url_rule("/contacts", view_func=get_contacts_api, methods=["GET"])

# POST → add contact
api.add_url_rule("/contact", view_func=create_contact_api, methods=["POST"])
