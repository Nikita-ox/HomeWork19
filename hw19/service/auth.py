from flask_restx import abort
from dao.auth import AuthDao
from utils import get_hash_from_password, generate_tokens, decode_token


class AuthService:
    def __init__(self, dao=AuthDao):
        self.dao = dao

    def login(self, data):
        user_data = self.dao.get_by_username(data["username"])
        if user_data is None:
            abort(401, message="user not found")

        hashed_password = get_hash_from_password(data["password"])
        if user_data.password != hashed_password:
            abort(401, message="Invalid credentials", )

        tokens = generate_tokens(
            {
                "username": user_data.username,
                "role": user_data.role
            }
        )
        return tokens

    def get_new_tokens(self, refresh_token):
        decoded_token = decode_token(refresh_token, refresh_token=True)
        tokens = generate_tokens(
            data={
                "username": decoded_token["username"],
                "role": decoded_token["role"],
            },
        )
        return tokens
