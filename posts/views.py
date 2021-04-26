from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from accounts.models import Userdetails
from faceshield.models import BluredImages


@login_required
def posts(request):
    data = Userdetails.objects.get(user=request.user)
    if BluredImages.objects.filter(user=request.user).exists():
        blur_data = BluredImages.objects.filter(user=request.user)
        blur_data = blur_data[len(blur_data) - 1]
        print(blur_data.blur_image.url)
    else:
        blur_data = None
    return render(request, 'posts/posts.html',{'data':data,'blur_data':blur_data})