from django.urls import path
from .views import PlanoDeTreinoView

urlpatterns = [
    path("planos-de-treino", PlanoDeTreinoView.as_view()),
]
