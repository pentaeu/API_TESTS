import requests
from utils.api_utils import ApiUtils


class MovieHelper:
    MOVIE_ENDPOINT = "/movies"

    def __init__(self, api_utils: ApiUtils) -> None:
        self.api_utils = api_utils

    def post_movie(self, json) -> requests.Response:
        response = self.api_utils.post(endpoint=self.MOVIE_ENDPOINT, json_body=json)

        return response

    def get_movies(self) -> requests.Response:
        response = self.api_utils.get(endpoint=self.MOVIE_ENDPOINT)

        return response

    def get_movie(self, movie_id) -> requests.Response:
        response = self.api_utils.get(endpoint=self.MOVIE_ENDPOINT + "/" + str(movie_id))

        return response
