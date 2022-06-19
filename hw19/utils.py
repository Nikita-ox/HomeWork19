import hashlib, base64
import jwt

from config import Config
from datetime import datetime, timedelta
from flask import request, current_app
from flask_restx import abort
from dao.auth import AuthDao


auth_dao = AuthDao()


def get_hash_from_password(password):  # В методе по дз несколько иначе реализован
    hashed_password: bytes = hashlib.pbkdf2_hmac(
        hash_name=Config.HASH_NAME,
        password=password.encode("utf-8"),
        salt=Config.SECRET_SALT.encode("utf-8"),
        iterations=Config.PWD_HASH_ITERATIONS
    )
    return base64.b64encode(hashed_password).decode("utf-8")


def generate_tokens(data):
    data["exp"] = datetime.utcnow() + timedelta(minutes=30)
    data["refresh_token"] = False

    access_token = jwt.encode(payload=data,
                              key=Config.SECRET,
                              algorithm=Config.JWT_ALGORITHM
                              )

    data["exp"] = datetime.utcnow() + timedelta(days=130)
    data["refresh_token"] = True

    refresh_token = jwt.encode(payload=data,
                               key=Config.SECRET,
                               algorithm=Config.JWT_ALGORITHM
                               )

    return {
        "access_token": access_token,
        "refresh_token": refresh_token
    }


def get_token_from_headers(headers: dict):
    if "Authorization" not in request.headers:
        abort(401)

    return headers["Authorization"].split(" ")[-1]


def decode_token(token: str, refresh_token: bool = False):
    decoded_token = {}
    try:
        decoded_token = jwt.decode(
            jwt=token,
            key=Config.SECRET,
            algorithms=[Config.JWT_ALGORITHM]
        )

    except jwt.PyJWTError:
        current_app.logger.info("Got wrong token: '%s'", token)
        abort(401)

    if decoded_token["refresh_token"] != refresh_token:
        abort(400, message="Got wrong token type")
    return decoded_token


def auth_required(func):
    def wrapper(*args, **kwargs):
        token = get_token_from_headers(request.headers)
        decoded_token = decode_token(token)

        if not auth_dao.get_by_username(decoded_token["username"]):
            abort(401)

        return func(*args, **kwargs)

    return wrapper


def admin_access_required(func):
    def wrapper(*args, **kwargs):
        token = get_token_from_headers(request.headers)
        decoded_token = decode_token(token)
        if decoded_token["role"] != "admin":
            abort(403)

        if not auth_dao.get_by_username(decoded_token["username"]):
            abort(401)

        return func(*args, **kwargs)

    return wrapper
