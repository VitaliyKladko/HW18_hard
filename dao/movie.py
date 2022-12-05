from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def get_all(self):
        all_movies_list = self.session.query(Movie).all()
        return all_movies_list

    def get_by_director_id(self, did):
        movie_by_director = self.session.query(Movie).filter(Movie.director_id == did)
        return movie_by_director

    def get_by_genre_id(self, gid):
        movie_by_genre = self.session.query(Movie).filter(Movie.genre_id == gid)
        # отдает list
        return movie_by_genre

    def get_by_year(self, m_year):
        movie_by_year = self.session.query(Movie).filter(Movie.year == m_year)
        return movie_by_year

    def create(self, data):
        """
        Метод получает на вход dict, создает новый экз. класса модели и добавляет его в БД
        :param data: dict
        :return: объект movie
        """
        new_movie = Movie(**data)
        self.session.add(new_movie)
        self.session.commit()
        return new_movie

    def update(self, movie):
        """
        Метод вызывается в сервисе и добавляет обновленный movie
        """
        self.session.add(movie)
        self.session.commit()
        return movie

    def delete(self, mid):
        movie_to_delete = self.session.query(Movie).get(mid)
        self.session.delete(movie_to_delete)
        self.session.commit()
