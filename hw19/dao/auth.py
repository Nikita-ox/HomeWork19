from setup_db import db
from dao.model.user import User


class AuthDao:
    def get_by_username(self, username):
        return db.session.query(User).filter(User.username == username).first()

