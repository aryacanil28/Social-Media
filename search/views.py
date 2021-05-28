from django.contrib.auth.models import User
from django.shortcuts import render,HttpResponse

# Create your views here.
from accounts.models import Userdetails
from faceshield.models import BluredImages
from posts.models import Posts, BluredPost


def getAllUsers(request):
    data = Userdetails.objects.get(user=request.user)
    if BluredImages.objects.filter(user=request.user).exists():
        blur_data = BluredImages.objects.filter(user=request.user)
        blur_data = blur_data[len(blur_data) - 1]
        print(blur_data.blur_image.url)
    else:
        blur_data = None
    if request.method =="POST" and len(request.POST['name']) > 0 :
        search_term = request.POST['name']
        result = Userdetails.objects.filter(display_name__contains=search_term)
    else:
        result = Userdetails.objects.all()
    return render(request,'search/results.html',{'result':result,'data':data,'blur_data':blur_data})


def searchByName():
    return None


def viewProfile(request,id):
    details = User.objects.get(id=id)
    data = Userdetails.objects.get(user=details)
    if BluredImages.objects.filter(user=details).exists():
        blur_data = BluredImages.objects.filter(user=details)
        blur_data = blur_data[len(blur_data) - 1]
        print(blur_data.blur_image.url)
    else:
        blur_data = None

    timeline = Posts.objects.filter(post_owner=details.id)
    print(timeline)
    BluredPosts = BluredPost.objects.filter(user=details)
    print(BluredPosts)
    timeline = reversed(timeline)
    print(timeline)

    return  render(request,'search/viewprofile.html',{'details':details,'data':data,'blur_data':blur_data,'timeline':timeline,'BluredPosts':BluredPosts})