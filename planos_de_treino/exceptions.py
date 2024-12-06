from rest_framework.exceptions import APIException
from rest_framework.views import status


class PlanoDeTreinoNotFound(APIException):
    default_data_field = "plano_de_treino_id"
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "%s not found."
    default_code = "not_found"

    def __init__(self, detail=None, code=None, data_field=None):
        detail = (
            self.default_detail % data_field
            if data_field
            else self.default_detail % self.default_data_field
        )

        super().__init__(detail, code)
