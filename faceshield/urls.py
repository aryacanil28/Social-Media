from django.urls import path
from . import views

urlpatterns = [
    path('auth-face/',views.faceAuthentification.as_view(),name='auth-face'),
]