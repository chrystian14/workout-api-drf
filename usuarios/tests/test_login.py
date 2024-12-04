from rest_framework.test import APITestCase
from rest_framework.views import status
import pytest

from usuarios.factories import RegularUserFactory
import factory


@pytest.mark.describe("POST /api/login")
class LoginTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.BASE_URL = "/api/login"

        cls.user_data = factory.build(dict, FACTORY_CLASS=RegularUserFactory)

        cls.created_user = RegularUserFactory.create(**cls.user_data)

    def test_login_with_valid_credencials(self):
        user_credentials = {
            "username": self.user_data["username"],
            "password": self.user_data["password"],
        }
        response = self.client.post(self.BASE_URL, data=user_credentials, format="json")

        expected_response_status_code = status.HTTP_200_OK
        resulted_response_status_code = response.status_code
        assert resulted_response_status_code == expected_response_status_code

    def test_token_fields_are_returned(self):
        user_credentials = {
            "username": self.user_data["username"],
            "password": self.user_data["password"],
        }
        response = self.client.post(self.BASE_URL, data=user_credentials, format="json")

        resulted_response_keys = response.json().keys()
        assert "access" in resulted_response_keys
        assert "refresh" in resulted_response_keys
