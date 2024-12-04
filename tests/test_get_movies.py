import requests

from logger.logger_main import Logger
from services.movie.helpers.movie_helper import MovieHelper
from services.movie.movies_api_service import MovieService


class TestGetMovies:
    def test_get_movies_status_code(self, api_utils_anonym_api):
        Logger.info("### Steps 1. Get movies")
        movie_helper = MovieHelper(api_utils_anonym_api)
        response = movie_helper.get_movies()

        assert response.status_code == requests.status_codes.codes.ok, \
            (f"Wrong status code. Actual: '{response.status_code}',"
             f" but expected: '{requests.status_codes.codes.ok}'")

    def test_get_movie(self, api_utils_anonym_api):
        movie_service = MovieService(api_utils=api_utils_anonym_api)
        Logger.info("### Steps 1. Get movies")
        response = movie_service.get_movies()
        Logger.info("### Steps 2. Get movie by id")
        first_movie_id = response.movies[0].id
        movie = movie_service.get_movie(first_movie_id)
        assert movie.id == first_movie_id, (f"Wrong movie id. Actual: '{movie.id}', "
                                            f"but expected: '{first_movie_id}'")
