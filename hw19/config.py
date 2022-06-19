class Config(object):
    DEBUG = True
    SECRET_SALT = "salt"
    SECRET = "secret_key"
    PWD_HASH_ITERATIONS = 100000
    HASH_NAME = "sha256"
    JWT_ALGORITHM = "HS256"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///movies.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RESTX_JSON = {"ensure_ascii": False, "indent": 3, "sort_keys": False}



