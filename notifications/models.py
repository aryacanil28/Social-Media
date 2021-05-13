from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from accounts.models import Userdetails
# Create your models here.
from posts.models import Posts


class Notifications(models.Model):
    notfication_id = models.AutoField(primary_key=True)
    reciver = models.ForeignKey(User, on_delete=models.CASCADE)
    sender = models.CharField(max_length=50,default=None,null=True)
    message = models.CharField(max_length=50,default=None,null=True)
    approved = models.BooleanField(('approved'), default=False)

    class Meta:
        verbose_name_plural = "Notifications"

    def __str__(self):
        return self.reciver.username

class PostNotifications(models.Model):
    notfication_id = models.AutoField(primary_key=True)
    post_id = models.ForeignKey(Posts, on_delete=models.CASCADE)
    reciver = models.ForeignKey(User, on_delete=models.CASCADE)
    sender = models.CharField(max_length=50, default=None, null=True)
    message = models.CharField(max_length=50, default=None, null=True)
    approved = models.BooleanField(('approved'), default=False)

    class Meta:
        verbose_name_plural = "Post Notifications"

    def __str__(self):
        return self.reciver.username

