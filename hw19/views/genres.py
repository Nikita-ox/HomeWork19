from flask_restx import Resource, Namespace
from flask import request
from dao.model.genre import GenreSchema
from implemented import genre_service
from utils import auth_required, admin_access_required


genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    @auth_required
    def get(self):
        rs = genre_service.get_all()
        res = GenreSchema(many=True).dump(rs)
        return res, 200

    @admin_access_required
    def post(self):
        req_data = request.json
        genre_service.create(req_data)
        return "", 201


@genre_ns.route('/<int:rid>')
class GenreView(Resource):
    @auth_required
    def get(self, rid):
        r = genre_service.get_one(rid)
        sm_d = GenreSchema().dump(r)
        return sm_d, 200

    @admin_access_required
    def put(self, rid):
        req_data = request.json
        req_data["id"] = rid
        genre_service.update(req_data)
        return "", 204

    @admin_access_required
    def delete(self, rid):
        return genre_service.delete(rid), 204