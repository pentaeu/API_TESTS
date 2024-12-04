import requests
from utils.api_utils import ApiUtils


class AuthorizationHelper:
    REGISTER_ENDPOINT = "/register"
    LOGIN_ENDPOINT = "/login"
    USER_ENDPOINT = "/user"

    def __init__(self, api_utils: ApiUtils):
        self.api_utils = api_utils

    def post_register(self, json) -> requests.Response:
        response = self.api_utils.post(endpoint=self.REGISTER_ENDPOINT, json_body=json)
        return response

    def post_login(self, json) -> requests.Response:
        response = self.api_utils.post(endpoint=self.LOGIN_ENDPOINT, json_body=json)
        return response

    def post_create_user(self, json) -> requests.Response:
        response = self.api_utils.post(endpoint=self.USER_ENDPOINT, json_body=json)
        return response
