"""AUTH Service Module"""

from services.auth.helpers.auth_helper import AuthorizationHelper
from services.auth.models.authorization.login_user_dto import LoginDto
from services.auth.models.registration.create_user_dto import CreateUserDto
from services.auth.models.registration.register_user_dto import RegisterDto
from services.auth.models.authorization.login_user_response import UserLoginResponse
from services.auth.models.registration.register_user_response import UserResponse


class AuthService:
    """
    Auth Service
    """

    def __init__(self, api_utils):
        """
        Init method
        :param api_utils: api utils
        """

        self.api_utils = api_utils

        self.authorization_helper = AuthorizationHelper(self.api_utils)

    def register_user(self, register_user: RegisterDto) -> UserResponse:
        """
        Register User
        :param register_user: RegisterDto
        :return: UserResponse
        """
        response = (self.authorization_helper.post_register
                    (register_user.model_dump(by_alias=True, exclude_defaults=False)))

        return UserResponse(**response.json())

    def login_user(self, login_user: LoginDto) -> UserLoginResponse:
        """
        Login User
        :param login_user: LoginDto
        :return: UserLoginResponse
        """
        response = (self.authorization_helper.post_login
                    (login_user.model_dump(by_alias=True, exclude_defaults=False)))

        return UserLoginResponse(**response.json())

    def create_user(self, created_user: CreateUserDto) -> UserResponse:
        """
        Create a user
        :param created_user: CreateUserDto
        :return: UserResponse
        """
        response = self.authorization_helper.post_create_user(created_user.model_dump(by_alias=True,
                                                                                      exclude_defaults=False))
        return UserResponse(**response.json())
