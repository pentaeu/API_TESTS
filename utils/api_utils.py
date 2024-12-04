import json

import curlify
import requests
from requests import Session

from logger.logger_main import Logger
from utils.json_utils import JsonUtils


def log_response(func):
    def _log_response(*args, **kwargs) -> requests.Response:
        """
        Log response data and other information
        """
        response = func(*args, **kwargs)
        Logger.info(f"Request curl: {curlify.to_curl(response.request)}")
        body = json.dumps(response.json(), indent=2, ensure_ascii=False) if JsonUtils.is_json(response.text) else response.text
        Logger.info(f"Response status code={response.status_code}, elapsed_time={response.elapsed}\n\n{body}\n")
        return response
    return _log_response


class ApiUtils:
    def __init__(self, url, headers=None):
        if headers is None:
            headers = {}

        self.session = Session()
        self.session.headers.update(headers)
        self.url = url


    def update_headers(self, headers) -> None:
        self.session.headers.update(headers)

    @log_response
    def get(self, endpoint, **kwargs) -> requests.Response:
        response = self.session.get(url=self.url + endpoint, **kwargs)
        return response

    @log_response
    def post(self, endpoint, data=None, json_body=None, **kwargs) -> requests.Response:
        response = self.session.post(self.url + endpoint, data, json_body, **kwargs)
        return response