from flask import current_app
from flask_login import UserMixin
from passlib.hash import pbkdf2_sha256 as hasher

class User(UserMixin):
    def __init__(self, mail, name, password, admin=False):
        self.id = mail
        self.name = name
        self.mail = mail
        self.password = hasher.hash(password)
        self.is_admin = admin

    def get_id(self):
        return self.mail

def find_user(mail):
    db = current_app.config["db"]
    user = [u for u in db.get_users() if u.mail == mail]
    if user:
        return user[0]
    return None