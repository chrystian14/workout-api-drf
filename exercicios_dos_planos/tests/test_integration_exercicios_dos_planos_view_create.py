from rest_framework.test import APITestCase
from rest_framework.views import status
from rest_framework_simplejwt.tokens import AccessToken
import pytest
from planos_de_treino.factories import PlanoDeTreinoFactory
from usuarios.factories import AdminUserFactory, RegularUserFactory
import factory
from unittest.mock import patch
from django.utils import timezone


@pytest.mark.describe("POST /api/exercicios-dos-planos")
class PlanoDeTreinoViewIntegrationTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.BASE_URL = "/api/exercicios-dos-planos"

        cls.super_user = AdminUserFactory(username="admin-user")
        cls.super_user_access_token = str(AccessToken.for_user(cls.super_user))

        cls.regular_user = RegularUserFactory.create(username="regular-user")
        cls.regular_user_access_token = str(AccessToken.for_user(cls.regular_user))

    def test_exercicios_do_plano_creation_without_token(self):
        response = self.client.post(self.BASE_URL, data={}, format="json")

        expected_status_code = status.HTTP_401_UNAUTHORIZED
        resulted_status_code = response.status_code
        assert resulted_status_code == expected_status_code

    def test_plano_de_treino_creation_with_non_admin_token(self):
        self.client.credentials(  # type: ignore
            HTTP_AUTHORIZATION="Bearer " + self.regular_user_access_token
        )

        response = self.client.post(self.BASE_URL, data={}, format="json")

        expected_status_code = status.HTTP_403_FORBIDDEN
        resulted_status_code = response.status_code
        assert resulted_status_code == expected_status_code

    def test_plano_de_treino_creation_with_missing_required_fields(self):
        plano_de_treino_data = {}

        self.client.credentials(  # type: ignore
            HTTP_AUTHORIZATION="Bearer " + self.super_user_access_token
        )
        response = self.client.post(
            self.BASE_URL, data=plano_de_treino_data, format="json"
        )

        expected_status_code = status.HTTP_400_BAD_REQUEST
        resulted_status_code = response.status_code
        assert resulted_status_code == expected_status_code

        expected_response_data = {
            "repeticoes": ["This field is required."],
            "series": ["This field is required."],
            "plano_de_treino_id": ["This field is required."],
            "exercicio_id": ["This field is required."],
        }
        resulted_response_data = response.json()
        assert resulted_response_data == expected_response_data

    # @patch("django.utils.timezone.now", return_value=timezone.now())
    # def test_plano_de_treino_creation_with_valid_data(self, mock_now):
    #     plano_de_treino_data = factory.build(
    #         dict, FACTORY_CLASS=PlanoDeTreinoFactory, usuario=self.regular_user
    #     )

    #     self.client.credentials(  # type: ignore
    #         HTTP_AUTHORIZATION="Bearer " + self.super_user_access_token
    #     )

    #     response = self.client.post(
    #         self.BASE_URL, data=plano_de_treino_data, format="json"
    #     )

    #     expected_status_code = status.HTTP_201_CREATED
    #     resulted_status_code = response.status_code
    #     assert resulted_status_code == expected_status_code

    #     expected_response_data = {
    #         "id": 1,
    #         "nome": plano_de_treino_data["nome"],
    #         "usuario": plano_de_treino_data["usuario"],
    #         "data_criacao": mock_now.return_value.isoformat().replace("+00:00", "Z"),
    #     }
    #     resulted_response_data = response.json()
    #     assert resulted_response_data == expected_response_data
