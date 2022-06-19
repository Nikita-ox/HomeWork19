from dao.user import UserDao
from utils import get_hash_from_password


class UserService:
    def __init__(self, dao: UserDao):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, user_data):
        user_data["password"] = get_hash_from_password(user_data.get("password"))
        return self.dao.create(user_data)

    def update(self, user_data):
        user_data["password"] = get_hash_from_password(user_data.get("password"))
        uid = user_data.get("id")
        user = self.get_one(uid)
        user.username = user_data.get("username")
        user.role = user_data.get("role")
        user.password = user_data.get("password")
        return self.dao.update(user)

    def delete(self, uid):
        return self.dao.delete(uid)

    # На всякий случай сравнение
    # def compare_pass(self, pass_hash, other_pass):
    #     decode_digest = base64.b64decode(pass_hash)
    #     hash_digest = hashlib.pbkdf2_hmac("sha256",
    #                                       other_pass.encode(),
    #                                       SECRET_HERE,
    #                                       PWD_HASH_ITERATIONS)
    #     return hmac.compare_digest(decode_digest, hash_digest)
