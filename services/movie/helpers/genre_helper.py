import requests

from utils.api_utils import ApiUtils


class GenreHelper:
    GENRE_ENDPOINT = "/genres"

    def __init__(self, api_utils: ApiUtils):
        self.api_utils = api_utils

    def post_genre(self, json) -> requests.Response:
        response = self.api_utils.post(endpoint=self.GENRE_ENDPOINT, json_body=json)
        return response
