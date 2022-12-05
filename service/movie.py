from dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def get_all(self):
        return self.dao.get_all()

    def get_by_director_id(self, did):
        return self.dao.get_by_director_id(did)

    def get_by_genre_id(self, gid):
        return self.dao.get_by_genre_id(gid)

    def get_by_year(self, m_year):
        return self.dao.get_by_year(m_year)

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        mid = data.get('id')
        movie_to_update = self.dao.get_one(mid)

        movie_to_update.title = data.get('title')
        movie_to_update.description = data.get('description')
        movie_to_update.trailer = data.get('trailer')
        movie_to_update.year = data.get('year')
        movie_to_update.rating = data.get('rating')
        movie_to_update.genre_id = data.get('genre_id')
        movie_to_update.director_id = data.get('director_id')

        self.dao.update(movie_to_update)

    def delete(self, mid):
        return self.dao.delete(mid)
