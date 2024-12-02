from django.urls import path
from .views import GrupoMuscularView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("grupos-musculares", GrupoMuscularView.as_view()),
]
