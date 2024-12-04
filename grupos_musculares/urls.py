from django.urls import path
from .views import GrupoMuscularView

urlpatterns = [
    path("grupos-musculares", GrupoMuscularView.as_view()),
]
