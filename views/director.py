from flask_restx import Resource, Namespace
from implemented import director_service
from dao.model.director import DirectorSchema

director_ns = Namespace('directors')
directors_schema = DirectorSchema(many=True)
director_schema = DirectorSchema()


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        all_director = director_service.get_all()
        return directors_schema.dump(all_director), 200


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did):
        one_director = director_service.get_one(did)

        if one_director is None:
            return {'error': 'Director not found'}, 404

        return director_schema.dump(one_director), 200
