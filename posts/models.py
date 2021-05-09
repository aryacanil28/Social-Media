import os

from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now
from datetime import date
# Create your models here.


def get_upload_postblur_path(instance,*args,**kwargs):
    return os.path.join('blured-post/{}/'.format(instance.user.first_name))


class Posts(models.Model):
    post_id = models.AutoField(primary_key=True)
    post_owner = models.ForeignKey(User,on_delete=models.CASCADE)
    post_image = models.FileField(upload_to="post_images",null=True)
    post_text = models.CharField(max_length=50,null=True)
    posted_time = models.TimeField(default=now(),editable=False)
    posted_date = models.DateField(default=date.today(),editable=False)
    post_likes = models.IntegerField(default=0)
    is_blur_post = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Posts Details"

    def __str__(self):
        return self.post_owner.username

class BluredPost(models.Model):
    blur_post_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blur_post = models.FileField(upload_to=get_upload_postblur_path, default=None, null=True)

    class Meta:
        verbose_name_plural = "Blured Post Details"

    def __str__(self):
        return self.user.username