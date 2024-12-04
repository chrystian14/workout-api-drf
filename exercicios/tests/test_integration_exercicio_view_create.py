from rest_framework.test import APITestCase
from rest_framework.views import status
from rest_framework_simplejwt.tokens import AccessToken
import pytest
from exercicios.factories import ExercicioFactory
from grupos_musculares.factories import GrupoMuscularFactory
from usuarios.factories import AdminUserFactory, RegularUserFactory
import factory


@pytest.mark.describe("POST /api/exercicios")
class ExercicioViewIntegrationTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.BASE_URL = "/api/exercicios"

        cls.super_user = AdminUserFactory(username="admin-user")
        cls.super_user_access_token = str(AccessToken.for_user(cls.super_user))

        cls.regular_user = RegularUserFactory.create(username="regular-user")
        cls.regular_user_access_token = str(AccessToken.for_user(cls.regular_user))

        cls.created_grupo_muscular = GrupoMuscularFactory.create(nome="Cardio")

    def test_exercicio_creation_without_token(self):
        exercicio_data = factory.build(dict, FACTORY_CLASS=ExercicioFactory)
        exercicio_data.update({"grupo_muscular": self.created_grupo_muscular.pk})

        response = self.client.post(self.BASE_URL, data=exercicio_data, format="json")

        expected_status_code = status.HTTP_401_UNAUTHORIZED
        resulted_status_code = response.status_code
        assert resulted_status_code == expected_status_code

    def test_exercicio_creation_with_non_admin_token(self):
        exercicio_data = factory.build(dict, FACTORY_CLASS=ExercicioFactory)
        exercicio_data.update({"grupo_muscular": self.created_grupo_muscular.pk})

        self.client.credentials(  # type: ignore
            HTTP_AUTHORIZATION="Bearer " + self.regular_user_access_token
        )

        response = self.client.post(self.BASE_URL, data=exercicio_data, format="json")

        expected_status_code = status.HTTP_403_FORBIDDEN
        resulted_status_code = response.status_code
        assert resulted_status_code == expected_status_code

    def test_exercicio_creation_with_valid_data(self):
        exercicio_data = factory.build(dict, FACTORY_CLASS=ExercicioFactory)
        exercicio_data.update({"grupo_muscular": self.created_grupo_muscular.pk})

        self.client.credentials(  # type: ignore
            HTTP_AUTHORIZATION="Bearer " + self.super_user_access_token
        )

        response = self.client.post(self.BASE_URL, data=exercicio_data, format="json")

        expected_status_code = status.HTTP_201_CREATED
        resulted_status_code = response.status_code
        assert resulted_status_code == expected_status_code

        expected_response_data = {
            "id": 1,
            "nome": exercicio_data["nome"],
            "descricao": exercicio_data["descricao"],
            "grupo_muscular": self.created_grupo_muscular.pk,
        }
        resulted_response_data = response.json()
        assert resulted_response_data == expected_response_data

    def test_exercicio_creation_with_missing_required_fields(self):
        exercicio_data = {}

        self.client.credentials(  # type: ignore
            HTTP_AUTHORIZATION="Bearer " + self.super_user_access_token
        )
        response = self.client.post(self.BASE_URL, data=exercicio_data, format="json")

        expected_status_code = status.HTTP_400_BAD_REQUEST
        resulted_status_code = response.status_code
        assert resulted_status_code == expected_status_code

        expected_response_data = {
            "nome": ["This field is required."],
            "grupo_muscular": ["This field is required."],
        }
        resulted_response_data = response.json()
        assert resulted_response_data == expected_response_data
