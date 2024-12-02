from rest_framework.test import APITestCase
from rest_framework.views import status
from pytest_check import check


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

        with check:
            expected_status_code = status.HTTP_201_CREATED
            resulted_status_code = response.status_code
            self.assertEqual(expected_status_code, resulted_status_code)

        with check:
            expected_response_data = {
                "id": 1,
                "username": user_data["username"],
                "email": user_data["email"],
                "first_name": user_data["first_name"],
                "last_name": user_data["last_name"],
                "is_superuser": user_data["is_superuser"],
            }
            resulted_response_data = response.json()
            self.assertEqual(expected_response_data, resulted_response_data)
