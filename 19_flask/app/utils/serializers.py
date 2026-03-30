def contact_to_dict(contact):
    return {
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
