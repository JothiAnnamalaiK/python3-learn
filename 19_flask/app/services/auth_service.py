from app.models.user import User
from app import db


def create_user(data):
    user = User(name=data.get("name"), email=data.get("email"))
    user.set_password(data.get("password"))

    db.session.add(user)
    db.session.commit()
    return user


def authenticate_user(email, password):
    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        return user
    return None
