from faker import Faker

from logger.logger_main import Logger
from services.auth.auth_api_service import AuthService
from services.auth.models.registration.create_user_dto import CreateUserDto

faker = Faker()


class TestCreateUser:
    def test_create_user(self, api_utils_super_admin_auth_api):
        auth_service = AuthService(api_utils=api_utils_super_admin_auth_api)

        Logger.info("### Steps 1. Create user")
        user = CreateUserDto(banned=False,
                             email=faker.email(),
                             full_name=faker.name(),
                             password=faker.password() + "aA1%",
                             verified=True)

        created_user = auth_service.create_user(user)
        assert created_user.email == user.email, (f"Wrong user email. Actual: '{created_user.email}', "
                                                  f"but expected: '{user.email}'")
