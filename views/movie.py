from flask_restx import Resource, Namespace
from dao.model.movie import MovieSchema
from implemented import movie_service
from flask import request


movie_ns = Namespace('movies')
movies_schema = MovieSchema(many=True)
movie_schema = MovieSchema()


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        all_movies = movie_service.get_all()

        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        year = request.args.get('year')

        if director_id is not None:
            all_movies = movie_service.get_by_director_id(director_id)

        if genre_id is not None:
            all_movies = movie_service.get_by_genre_id(genre_id)

        if year is not None:
            all_movies = movie_service.get_by_year(year)

        return movies_schema.dump(all_movies), 200

    def post(self):
        data_json = request.json
        new_film = movie_service.create(data_json)
        return '', 201, {'new_film': f'/movie/id:{new_film.id}'}


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        movie = movie_service.get_one(mid)

        if movie is None:
            return {'error': 'Movie not found'}, 404

        return movie_schema.dump(movie), 200

    def put(self, mid):
        data_json = request.json
        data_json['id'] = mid
        movie_service.update(data_json)

        required_fields = ['description', 'year', 'title', 'genre_id', 'director_id', 'trailer', 'rating']

        for field in required_fields:
            if field not in data_json:
                return {'error': f'Поле {field} обязательно для заполнения'}, 400

        return '', 204

    def delete(self, mid):
        movie_to_delete = movie_service.get_one(mid)

        if movie_to_delete is None:
            return {"error": "Movie not found"}, 404

        movie_service.delete(mid)
        return '', 204
