from flask import request
from flask_restx import Resource, Namespace
from implemented import user_service
from dao.model.user import UserSchema
from utils import auth_required, admin_access_required


ns_user = Namespace("users")


@ns_user.route("/")
class UsersView(Resource):
    @auth_required
    def get(self):
        all_users = user_service.get_all()
        result = UserSchema(many=True).dump(all_users)
        return result, 200

    def post(self):
        req_data = request.json
        user = user_service.create(req_data)
        return "", 201, {"location": f"/users/{user.id}"}


@ns_user.route("/<int:uid>")
class UserView(Resource):
    @auth_required
    def get(self, uid):
        user = user_service.get_one(uid)
        return UserSchema().dump(user), 200

    @admin_access_required
    def put(self, uid):
        req_data = request.json
        req_data["id"] = uid
        user_service.update(req_data)
        return "", 204

    @admin_access_required
    def patch(self, uid):
        req_data = request.json
        req_data["id"] = uid
        user_service.update(req_data)
        return "", 204

    @admin_access_required
    def delete(self, uid):
        user_service.delete(uid)
        return "", 204

