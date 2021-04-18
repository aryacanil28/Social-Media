from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from django.views import View
from django.contrib.auth.models import User
from .models import Userdetails,Shield,Facelearn
from django.contrib.auth import settings
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
# Create your views here.

class signup(View):

    def post(self,request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        confirm_email = request.POST['confirm_email']
        password = request.POST['password']
        gender = request.POST['gender']
        dob = request.POST['dob']

        if email == confirm_email:

            if User.objects.filter(email=email).exists():
                messages.error(request, '! email taken.')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=first_name + last_name, first_name=first_name,
                                                last_name=last_name, email=email, password=password)
                user.save()
                profile = Userdetails(user=user, gender=gender, date_of_birth=dob,display_name=first_name + last_name,profile_pic="profile-pic/avathar.png")
                profile.save()
                return redirect('signin')
        else:
            messages.error(request,'! email doesn\'t match.')
            return redirect('signup')

    def get(self, request):
        return render(request, 'accounts/signup.html')


class signin(View):

   def post(self,request):
       login_email = request.POST['email']
       login_password = request.POST['password']

       if User.objects.filter(email=login_email).exists():
           user = User.objects.get(email=login_email)
           print(user)
           print(user.check_password(login_password))
           if user.check_password(login_password):

               if user:
                    auth.login(request,user)
                    return redirect(settings.LOGIN_REDIRECT_URL)

           else:

               return render(request,'accounts/signin.html',{'error':"! invalid password "})
       else:

           return render(request, 'accounts/signin.html', {'error': "! invalid email "})

   def get(self,request):
        return render(request, 'accounts/signin.html',{'error':""})


class profile(View):
    def get(self, request):
        # print(request.user.id)
        data = Userdetails.objects.get(user=request.user)
        # print(data.id)
        # print(data.profile_pic.url)
        return render(request, 'accounts/profile.html',{'data':data})



@login_required
def logout(request):
    auth.logout(request)
    return redirect('signin')

@login_required
def editProfile(request):
    data = Userdetails.objects.get(user=request.user)
    if Shield.objects.filter(user=request.user):
        shield = Shield.objects.get_or_none(user=request.user)
        obj = Facelearn.objects.get(user=request.user)
        number_of_imgs = obj.number_of_images
        percent = (number_of_imgs*100)/20
    if request.method == 'POST':
        data.profile_pic=request.FILES['newprofile']
        data.save()
    return render(request, 'accounts/edit-profile.html',{'data':data,'shield':shield,'number_of_imgs':number_of_imgs,'percent':percent })

@login_required
def activateShield(request):
    shield = Shield.objects.get(user=request.user)
    shield.active=True
    shield.save()
    obj = Facelearn.objects.get_or_create(user=request.user)
    obj.save()
    return redirect('editProfile')

@login_required
def deactivateShield(request):
    shield = Shield.objects.get(user=request.user)
    shield.active=False
    shield.save()
    return redirect('editProfile')

def uploadTrainingData(request):
    if request.method == 'POST':
        if Facelearn.objects.get(user=request.user):
            obj = Facelearn.objects.get(user=request.user)
            obj.face_training = request.FILES['face_training']
            print(obj.number_of_images)
            obj.number_of_images = obj.number_of_images + 1
            obj.save()
            number_of_imgs = obj.number_of_images
            shield = Shield.objects.get(user=request.user)
            if number_of_imgs < 10:
                shield.danger = True
            elif number_of_imgs >= 10 and number_of_imgs <= 14 :
                shield.danger = False
                shield.warning = True
            elif number_of_imgs > 14:
                shield.danger = False
                shield.warning = False
            shield.save()

        return redirect('editProfile')

       #  obj = Facelearn.objects.create(user=request.user)
       #  obj.save()
       #  return redirect('editProfile')

    return redirect('editProfile')