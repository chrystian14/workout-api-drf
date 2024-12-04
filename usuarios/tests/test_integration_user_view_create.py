from rest_framework.test import APITestCase
from rest_framework.views import status
import pytest
import factory

from usuarios.factories import RegularUserFactory, UserFactory


@pytest.mark.describe("POST /api/users")
class UserViewIntegrationTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.BASE_URL = "/api/users"

    def test_user_creation_with_valid_data(self):
        user_data = factory.build(dict, FACTORY_CLASS=RegularUserFactory)
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
        duplicated_username = "naruto"

        RegularUserFactory.create(
            username=duplicated_username,
        )

        user_with_duplicated_username_data = factory.build(
            dict, FACTORY_CLASS=RegularUserFactory, username=duplicated_username
        )

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
        duplicated_email = "itachi@mail.com"

        RegularUserFactory.create(
            email=duplicated_email,
        )

        user_with_duplicated_email_data = factory.build(
            dict, FACTORY_CLASS=RegularUserFactory, email=duplicated_email
        )

        response = self.client.post(
            self.BASE_URL, data=user_with_duplicated_email_data, format="json"
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
        user_data_with_invalid_email = factory.build(
            dict, FACTORY_CLASS=RegularUserFactory, email="invalid-email-format"
        )

        response = self.client.post(
            self.BASE_URL, data=user_data_with_invalid_email, format="json"
        )

        expected_response_data = {
            "email": ["Enter a valid email address."],
        }
        resulted_response_data = response.json()
        assert resulted_response_data == expected_response_data
