import unittest

from rowantree.common.sdk import demand_env_var
from src.rowantree.auth.sdk import AuthenticateUserCommand, AuthenticateUserRequest, Token


class TestRegisterUser(unittest.TestCase):
    def test_auth_user(self):
        auth_user_command: AuthenticateUserCommand = AuthenticateUserCommand()

        request: AuthenticateUserRequest = AuthenticateUserRequest(
            username=demand_env_var("ACCESS_USERNAME"), password=demand_env_var("ACCESS_PASSWORD")
        )
        token: Token = auth_user_command.execute(request=request)
        print(token)


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(TestRegisterUser())
