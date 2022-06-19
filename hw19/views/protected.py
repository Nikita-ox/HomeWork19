# Файл из разбора ДЗ, частично дублирует user View

from flask_restx import Resource, Namespace
from dao.model.user import UserSchema
from implemented import user_service
from utils import auth_required, admin_access_required


ns_protected = Namespace("protected")


@ns_protected.route("/users")
class UsersView(Resource):
    @auth_required
    def get(self):
        all_users = user_service.get_all()
        result = UserSchema(many=True).dump(all_users)
        return result, 200


@ns_protected.route("/admin")
class AdminView(Resource):
    @admin_access_required
    def get(self):
        all_users = user_service.get_all()
        result = UserSchema(many=True).dump(all_users)
        return result, 200

