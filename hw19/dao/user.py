from dao.model.user import User


class UserDao:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(User).get(uid)

    def get_all(self):
        return self.session.query(User).all()

    def create(self, user_data):
        new_user = User(**user_data)
        self.session.add(new_user)
        self.session.commit()
        return new_user

    def update(self, user):
        self.session.add(user)
        self.session.commit()
        return user

    def delete(self, uid):
        user = self.session.query(User).get(uid)
        self.session.delete(user)
        self.session.commit()

