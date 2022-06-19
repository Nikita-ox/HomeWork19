from flask_restx import Resource, Namespace
from flask import request
from implemented import auth_service
ns_auth = Namespace("auth")


@ns_auth.route("/")
class AuthView(Resource):
    def post(self):
        return auth_service.login(request.json)

    def put(self):
        return auth_service.get_new_tokens(request.json["refresh_token"])