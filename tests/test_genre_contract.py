import requests
from faker import Faker

from services.movie.helpers.genre_helper import GenreHelper

faker = Faker()


class TestGenreContract:
    def test_genre_contract_anonym(self, api_utils_anonym_api):
        genre_helper = GenreHelper(api_utils=api_utils_anonym_api)
        response = genre_helper.post_genre({"name": faker.name()})

        assert response.status_code == requests.status_codes.codes.unauthorized, \
            (f"Wrong status code. Actual: '{response.status_code}',"
             f" but expected: '{requests.status_codes.codes.unauthorized}'")
