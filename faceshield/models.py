
import os

from django.db import models
from django.contrib.auth.models import User
from accounts.models import Userdetails
# Create your models here.

def get_upload_path(instance,*args,**kwargs):
    return os.path.join('face_training/s{0}/{1}'.format(instance.user.id,args[0]))

def get_upload_blur_path(instance,*args,**kwargs):
    return os.path.join('Blured/{}/'.format(instance.user.first_name))

class BluredImages(models.Model):
    blur_image_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blur_image = models.FileField(upload_to=get_upload_blur_path, default=None, null=True)

    class Meta:
        verbose_name_plural = "Blured Images Details"

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


class FaceShieldDetails(models.Model):
    user_fsd = models.ForeignKey(User, on_delete=models.CASCADE)
    userdetails_fsd = models.ForeignKey(Userdetails, on_delete=models.CASCADE)
    shield_fsd = models.ForeignKey(Shield, on_delete=models.CASCADE)
    facelearn_fsd = models.ForeignKey(Facelearn, on_delete=models.CASCADE)
    folder_fsd = models.CharField(max_length=20,default=None,null=True)

    class Meta:
        verbose_name_plural = "Face Shield Details"

    def __str__(self):
        return self.user_fsd.username