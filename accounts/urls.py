from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.signup.as_view(),name='signup'),
    path('signin/', views.signin.as_view(), name='signin'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile.as_view(), name='profile'),
    path('edit-profile/', views.editProfile, name='editProfile'),
    path('activate-shield/',views.activateShield,name='activate-shield'),
    path('deactivate-shield/',views.deactivateShield,name='deactivate-shield'),
    path('upload-training-data/', views.uploadTrainingData, name='uploadTrainingData')
]