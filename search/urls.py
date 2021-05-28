from django.urls import path
from . import views

urlpatterns = [
    path('', views.getAllUsers, name='search'),
    path('view-profile/<int:id>', views.viewProfile, name='viewProfile'),
    path('<str:name>', views.searchByName, name="uploadPost")
]
