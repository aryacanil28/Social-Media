
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

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


