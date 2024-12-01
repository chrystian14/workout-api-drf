from math import exp
from rest_framework.test import APITestCase
from rest_framework.views import status
import pytest


@pytest.mark.describe("POST /api/users")
class UserViewIntegrationTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.BASE_URL = "/api/users"

    def test_user_creation_with_valid_data(self):
        user_data = {
            "username": "john14",
            "password": "my_secret_password",
            "email": "john-doe@mail.com.br",
            "first_name": "John",
            "last_name": "Doe",
            "is_superuser": False,
        }

        response = self.client.post(self.BASE_URL, data=user_data, format="json")

        expected_status_code = status.HTTP_201_CREATED
        resulted_status_code = response.status_code
        assert resulted_status_code == expected_status_code

        expected_response_data = {
            "id": 1,
            "username": user_data["username"],
            "email": user_data["email"],
            "first_name": user_data["first_name"],
            "last_name": user_data["last_name"],
            "is_superuser": user_data["is_superuser"],
        }
        resulted_response_data = response.json()
        assert resulted_response_data == expected_response_data

    def test_user_creation_with_missing_required_fields(self):
        user_data = {}

        response = self.client.post(self.BASE_URL, data=user_data, format="json")

        expected_status_code = status.HTTP_400_BAD_REQUEST
        resulted_status_code = response.status_code
        assert resulted_status_code == expected_status_code

        expected_response_data = {
            "username": ["This field is required."],
            "password": ["This field is required."],
            "email": ["This field is required."],
            "first_name": ["This field is required."],
            "last_name": ["This field is required."],
            "is_superuser": ["This field is required."],
        }
        resulted_response_data = response.json()
        assert resulted_response_data == expected_response_data

    def test_user_creation_with_existing_username(self):
        user_data = {
            "username": "john14",
            "password": "my_secret_password",
            "email": "john-doe@mail.com.br",
            "first_name": "John",
            "last_name": "Doe",
            "is_superuser": False,
        }

        user_with_duplicated_username_data = {
            **user_data,
            "email": "another@email.com",
        }

        self.client.post(self.BASE_URL, data=user_data, format="json")

        response = self.client.post(
            self.BASE_URL, data=user_with_duplicated_username_data, format="json"
        )

        expected_status_code = status.HTTP_400_BAD_REQUEST
        resulted_status_code = response.status_code
        assert resulted_status_code == expected_status_code

        expected_response_data = {
            "username": ["A user with that username already exists."],
        }
        resulted_response_data = response.json()
        assert resulted_response_data == expected_response_data

    def test_user_creation_with_existing_email(self):
        user_data = {
            "username": "john14",
            "password": "my_secret_password",
            "email": "john-doe@mail.com.br",
            "first_name": "John",
            "last_name": "Doe",
            "is_superuser": False,
        }

        user_with_same_email_data = {**user_data, "username": "john15"}

        self.client.post(self.BASE_URL, data=user_data, format="json")

        response = self.client.post(
            self.BASE_URL, data=user_with_same_email_data, format="json"
        )

        expected_status_code = status.HTTP_400_BAD_REQUEST
        resulted_status_code = response.status_code
        assert resulted_status_code == expected_status_code

        expected_response_data = {
            "email": ["A user with that email already exists."],
        }
        resulted_response_data = response.json()
        assert resulted_response_data == expected_response_data

    def test_user_creation_with_invalid_email(self):
        user_data = {
            "username": "john14",
            "password": "my_secret_password",
            "email": "invalid-email",
            "first_name": "John",
            "last_name": "Doe",
            "is_superuser": False,
        }

        response = self.client.post(self.BASE_URL, data=user_data, format="json")

        expected_response_data = {
            "email": ["Enter a valid email address."],
        }
        resulted_response_data = response.json()
        assert resulted_response_data == expected_response_data
