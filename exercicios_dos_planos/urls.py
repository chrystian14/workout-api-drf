from django.urls import path
from .views import ExercicioDoPlanoView

urlpatterns = [
    path("exercicios-dos-planos", ExercicioDoPlanoView.as_view()),
]
