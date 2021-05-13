from django.contrib import admin

from .models import Notifications,PostNotifications
# Register your models here.

admin.site.register(Notifications)
admin.site.register(PostNotifications)