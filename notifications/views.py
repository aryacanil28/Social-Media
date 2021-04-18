from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from accounts.models import Userdetails


@login_required
def notification(request):
    data = Userdetails.objects.get(user=request.user)
    return render(request, 'notifications/notification.html',{'data':data})