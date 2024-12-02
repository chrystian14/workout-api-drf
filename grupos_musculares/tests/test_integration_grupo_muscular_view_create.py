from math import exp
from rest_framework.test import APITestCase
from rest_framework.views import status
import pytest


@pytest.mark.describe("POST /api/grupos-musculares")
class GrupoMuscularViewIntegrationTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.BASE_URL = "/api/grupos-musculares"

    def test_grupo_muscular_creation_without_token(self):
        grupo_muscular_data = {
            "nome": "Cardio",
            "descricao": "Exercícios de cardiovascular",
        }

        response = self.client.post(
            self.BASE_URL, data=grupo_muscular_data, format="json"
        )

        expected_status_code = status.HTTP_401_UNAUTHORIZED
        resulted_status_code = response.status_code
        assert resulted_status_code == expected_status_code

    def test_grupo_muscular_creation_with_valid_data(self):
        grupo_muscular_data = {
            "nome": "Cardio",
            "descricao": "Exercícios de cardiovascular",
        }

        response = self.client.post(
            self.BASE_URL, data=grupo_muscular_data, format="json"
        )

        expected_status_code = status.HTTP_201_CREATED
        resulted_status_code = response.status_code
        assert resulted_status_code == expected_status_code

        expected_response_data = {
            "id": 1,
            "nome": grupo_muscular_data["nome"],
            "descricao": grupo_muscular_data["descricao"],
        }
        resulted_response_data = response.json()
        assert resulted_response_data == expected_response_data

    def test_grupo_muscular_creation_with_missing_required_fields(self):
        grupo_muscular_data = {}

        response = self.client.post(
            self.BASE_URL, data=grupo_muscular_data, format="json"
        )

        expected_status_code = status.HTTP_400_BAD_REQUEST
        resulted_status_code = response.status_code
        assert resulted_status_code == expected_status_code

        expected_response_data = {
            "nome": ["This field is required."],
        }
        resulted_response_data = response.json()
        assert resulted_response_data == expected_response_data
