from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib.auth.models import User
from accounts.models import Userdetails
from faceshield.models import BluredImages
from .models import Notifications

@login_required
def notification(request):
    data = Userdetails.objects.get(user=request.user)
    notification = Notifications.objects.filter(reciver=request.user,approved=False)
    if BluredImages.objects.filter(user=request.user).exists():
        blur_data = BluredImages.objects.filter(user=request.user)
        blur_data = blur_data[len(blur_data) - 1]
        print(blur_data.blur_image.url)
    else:
        blur_data = None
    return render(request, 'notifications/notification.html',{'data':data, 'nfs':notification,'blur_data':blur_data})

@login_required
def acceptNf(request,id):
    print(id)
    nfs = Notifications.objects.get(notfication_id=id, approved=False)
    nfs.approved = True
    nfs.save()
    other_user = User.objects.get(username=nfs.sender)
    accept= Userdetails.objects.get(user= other_user)
    if not Notifications.objects.filter(sender=accept.user.username,approved=False):
        accept.Blur_dp=False
        accept.save()
        return redirect('notifications')

@login_required
def rejectNf(request, id):
    Notifications.objects.get(notfication_id=id, approved=False).delete()
    return redirect('notifications')