from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from accounts.models import Userdetails
from faceshield.models import BluredImages, Shield
from faceshield.views import faceAuthentification
from notifications.models import Notifications, PostNotifications
from .models import Posts, BluredPost


@login_required
def posts(request):
    data = Userdetails.objects.get(user=request.user)
    if BluredImages.objects.filter(user=request.user).exists():
        blur_data = BluredImages.objects.filter(user=request.user)
        blur_data = blur_data[len(blur_data) - 1]
        print(blur_data.blur_image.url)
    else:
        blur_data = None

    timeline = Posts.objects.all()
    BluredPosts = BluredPost.objects.all()
    timeline = reversed(timeline)
    return render(request, 'posts/posts.html',{'data':data,'blur_data':blur_data,'timeline':timeline,'BluredPosts':BluredPosts})

@login_required
def uploadPost(request):
    if request.method == 'POST':

        if request.POST['post_text'] != '' and request.FILES['post_image'] != '':
            post_image = request.FILES['post_image']
            post_text = request.POST['post_text']
            post = Posts()
            post.post_text = post_text
            post.post_image = post_image
            post.post_owner_id = request.user.id
            post.save()

            fds_post = faceAuthentification(request,'post_image')
            result = fds_post.fds()
            if result:
                data = Userdetails.objects.get(user=request.user)
                print('result', result)
                for u_name in result:
                    if u_name != data.user.first_name:
                        if User.objects.filter(first_name=u_name).exists():
                            user = User.objects.get(first_name=u_name)
                            if Shield.objects.filter(user=user).exists():
                                obj_user = Shield.objects.get(user=user)
                                print(obj_user.active)
                                if obj_user.active:
                                    fds_post.bluring_faces(request, 'post_image', post)
                                    post_ob = Posts.objects.filter(post_owner=request.user)
                                    latest_pst = post_ob[len(post_ob) - 1]
                                    latest_pst.is_blur_post = True
                                    latest_pst.save()

                                    print("send  notification")
                                    msg = "{} Posted a photo with a face similar to you, Please verify now.".format(
                                        request.user.username)
                                    PostNotifications.objects.create(reciver=user, sender=request.user.username,
                                                                 message=msg,post_id=post).save()

        else:
            return redirect('profile')

    return redirect('posts')