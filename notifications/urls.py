from django.urls import path
from . import views

urlpatterns = [
    path('notification/',views.notification,name='notifications'),
    path('accept/<int:id>',views.acceptNf,name='accept'),
    path('reject/<int:id>',views.rejectNf,name='reject'),
    path('post-accept/<int:id>',views.post_acceptNf,name='post-accept'),
    path('post-reject/<int:id>',views.post_rejectNf,name='post-reject'),
]