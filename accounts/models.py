import os

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
def get_upload_path(instance,*args,**kwargs):
    return os.path.join('face_training/s{0}/{1}'.format(instance.user.id,args[0]))

class Userdetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=20,default=None,null=True)
    gender = models.CharField(max_length=6,default=None)
    contact = models.CharField(max_length=10,default=None,null=True)
    date_of_birth = models.DateField(default=None)
    loaction = models.CharField(max_length=50,default=None,null=True)
    city = models.CharField(max_length=20,default=None,null=True)
    state = models.CharField(max_length=20,default=None,null=True)
    country = models.CharField(max_length=20,default=None,null=True)
    profile_pic = models.FileField(upload_to="profile-pic",default=None,null=True)
    profile_pic_blur = models.FileField(upload_to="profile-pic-blur", default=None, null=True)
    cover_pic = models.FileField(upload_to="cover-pic", default=None, null=True)
    Blur_dp = models.BooleanField(('blur profile pic'), default=False)
    is_online = models.BooleanField(('online'), default=False)

    class Meta:
        verbose_name_plural = "User Details"

    def __str__(self):
        return self.user.username



class Shield(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pending = models.BooleanField(('pending'), default=False)
    active = models.BooleanField(('active'), default=False)
    danger = models.BooleanField(('danger'), default=False)
    warning = models.BooleanField(('warning'), default=False)

    class Meta:
        verbose_name_plural = "Shield Details"

    def __str__(self):
        return self.user.username


class Facelearn(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    face_training = models.FileField(upload_to=get_upload_path, default=None, null=True)
    number_of_images = models.IntegerField(default=0,null=True)

    class Meta:
        verbose_name_plural = "Facelearn Details"

    def __str__(self):
        return self.user.username