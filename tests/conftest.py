import os

import pytest

from configs.urls_config import AUTH_URL, MOVIE_URL
from services.auth.auth_api_service import AuthService
from services.auth.models.authorization.login_user_dto import LoginDto
from utils.api_utils import ApiUtils


@pytest.fixture(scope="session", autouse=False)
def api_utils_anonym_auth():
    api_utils_anonym = ApiUtils(url=AUTH_URL)
    yield api_utils_anonym


@pytest.fixture(scope="session", autouse=False)
def api_utils_anonym_api():
    api_utils_anonym = ApiUtils(url=MOVIE_URL)
    yield api_utils_anonym


@pytest.fixture(scope="session", autouse=False)
def api_utils_super_admin_movie_api(api_utils_anonym_auth):
    email = os.environ["USER_EMAIL"]
    password = os.environ["USER_PASSWORD"]

    auth_service = AuthService(api_utils=api_utils_anonym_auth)
    login_user = LoginDto(email=email, password=password)
    login_response = auth_service.login_user(login_user)

    api_utils_super_admin = ApiUtils(url=MOVIE_URL,
                                     headers={"Authorization": f"Bearer {login_response.access_token}"})
    yield api_utils_super_admin


@pytest.fixture(scope="session", autouse=False)
def api_utils_super_admin_auth_api(api_utils_anonym_auth):
    email = os.environ["USER_EMAIL"]
    password = os.environ["USER_PASSWORD"]

    auth_service = AuthService(api_utils=api_utils_anonym_auth)
    login_user = LoginDto(email=email, password=password)
    login_response = auth_service.login_user(login_user)

    api_utils_super_admin = ApiUtils(url=AUTH_URL,
                                     headers={"Authorization": f"Bearer {login_response.access_token}"})
    yield api_utils_super_admin
