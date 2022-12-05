from flask_restx import Resource, Namespace
from dao.model.genre import GenreSchema
from implemented import genre_service


genre_ns = Namespace('genres')
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        all_genre = genre_service.get_all()
        return genres_schema.dump(all_genre), 200


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        one_genre = genre_service.get_one(gid)

        if one_genre is None:
            return {'error': 'Genre not found'}, 404

        return genre_schema.dump(one_genre), 200
