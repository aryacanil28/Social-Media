from django.urls import path
from . import views

urlpatterns = [
    path('post/',views.posts,name='posts'),
    path('uploadPost/',views.uploadPost,name="uploadPost")
]