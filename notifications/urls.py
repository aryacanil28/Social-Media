from django.urls import path
from . import views

urlpatterns = [
    path('notification/',views.notification,name='notifications'),
    path('accept/<int:id>',views.acceptNf,name='accept'),
    path('reject/<int:id>',views.rejectNf,name='reject'),
]