from dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, bid):
        return self.dao.get_one(bid)

    def get_all(self):
        # if filters.get("director_id") is not None:
        #     movies = self.dao.get_by_director_id(filters.get("director_id"))
        # elif filters.get("genre_id") is not None:
        #     movies = self.dao.get_by_genre_id(filters.get("genre_id"))
        # elif filters.get("year") is not None:
        #     movies = self.dao.get_by_year(filters.get("year"))
        # else:
        #     movies = self.dao.get_all()
        return self.dao.get_all()

    def get_by_director(self, director_id):
        return self.dao.get_by_director_id(director_id)

    def get_by_genre(self, genre_id):
        return self.dao.get_by_genre_id(genre_id)

    def get_by_year(self, year):
        return self.dao.get_by_year(year)

    def create(self, movie_d):
        return self.dao.create(movie_d)

    def update(self, movie_d):
        self.dao.update(movie_d)
        return self.dao

    def delete(self, rid):
        self.dao.delete(rid)
