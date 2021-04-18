from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from accounts.models import Userdetails


@login_required
def posts(request):
    data = Userdetails.objects.get(user=request.user)
    return render(request, 'posts/posts.html',{'data':data})