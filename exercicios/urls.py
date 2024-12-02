from django.urls import path
from .views import ExercicioView

urlpatterns = [
    path("exercicios", ExercicioView.as_view()),
]
