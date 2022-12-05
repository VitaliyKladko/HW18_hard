from dao.model.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, did):
        director = self.session.query(Director).get(did)
        return director

    def get_all(self):
        director_list = self.session.query(Director).all()
        return director_list
