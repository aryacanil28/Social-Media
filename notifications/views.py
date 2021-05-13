from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib.auth.models import User
from accounts.models import Userdetails
from faceshield.models import BluredImages
from posts.models import Posts
from .models import Notifications,PostNotifications


@login_required
def notification(request):
    data = Userdetails.objects.get(user=request.user)
    notification = Notifications.objects.filter(reciver=request.user,approved=False)
    post_notifications = PostNotifications.objects.filter(reciver=request.user,approved=False)
    if BluredImages.objects.filter(user=request.user).exists():
        blur_data = BluredImages.objects.filter(user=request.user)
        blur_data = blur_data[len(blur_data) - 1]
        print(blur_data.blur_image.url)
    else:
        blur_data = None
    return render(request, 'notifications/notification.html',{'data':data, 'nfs':notification,'blur_data':blur_data,'post_notifications':post_notifications})

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


def post_acceptNf(request, id):
    print(id)
    pst_nfs = PostNotifications.objects.get(notfication_id=id, approved=False)
    pst_nfs.approved = True
    pst_nfs.save()

    post_obj = Posts.objects.get(post_id=pst_nfs.post_id.post_id)
    if not PostNotifications.objects.filter(post_id=post_obj.post_id, approved=False):
        post_obj.is_blur_post = False
        post_obj.save()
        return redirect('notifications')


def post_rejectNf(request, id):
    PostNotifications.objects.get(notfication_id=id, approved=False).delete()
    return redirect('notifications')