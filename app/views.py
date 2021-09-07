from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
import random
from django.contrib.auth.models import Group, Permission
from django.views import View
from rest_framework.generics import ListAPIView
from django.core import validators
from django.views.generic.edit import UpdateView
from rest_framework import filters
from django.utils.decorators import method_decorator
global num4
from django.contrib.auth.mixins import LoginRequiredMixin
class register(View):
    def get(self, request):
        num1 = (random.randint(1, 10))
        num2 = (random.randint(1, 10))
        num3 = str(str(num1) + "+" + str(num2))
        global num4
        num4 = num1 + num2
        print(num4)
        return render(request, 'esss//resgister.html', {"img": num3})
    def post(self,request):
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        cap = request.POST.get("captha")
        image = request.FILES.get('image', "")
        global num4
        if image is None:
            user = User.objects.filter(username=username).exists()
            if not username.isalnum():
                messages.error(request, 'Username Should only contain letters and number ')
                return redirect('sigin')
            if len(pass1) < 8:
                messages.error(request, "password length to at least a value of 8")
                return redirect('sigin')
            if pass1 != pass2:
                messages.error(request, 'Password do no match')
                return redirect('sigin')
            if user:
                messages.error(request, "Username  is already exits ")
                return redirect('sigin')

            if str(cap) != str(num4):
                messages.error(request, 'Error captha')
                return redirect('sigin')
            myuser = User.objects.create_user(username, email, pass1)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            messages.success(request, "You account has been successfuly created")
            return redirect("login")
        else:
            user = User.objects.filter(username=username).exists()
            if not username.isalnum():
                messages.error(request, 'Username Should only contain letters and number ')
                return redirect('sigin')
            if len(pass1) < 8:
                messages.error(request, "password length to at least a value of 8")
                return redirect('sigin')
            if pass1 != pass2:
                messages.error(request, 'Password do no match')
                return redirect('sigin')
            if user:
                messages.error(request, "Username  is already exits ")
                return redirect('sigin')
            if str(cap) != str(num4):
                messages.error(request, 'Error captha')
                return redirect('sigin')
            myuser = User.objects.create_user(username, email, pass1)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.image = image
            myuser.is_staff = True
            myuser.save()
            messages.success(request, "You account has been successfuly created")
            return redirect("login")




class login(View):
    def get(self, request):
        return render(request, 'esss/login.html')



    def post(self, request):
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            auth_login(request, user)
            messages.success(request, "Successfuly Logged  In")
            return redirect('home')
        else:
            messages.success(request, "Invaild  Credentials, Please try again")
            return redirect('login')


@login_required(login_url='/login/')
def home(request):
    try:
        user=request.user
        user1=User.objects.all().get(id=user.id)
        print(user1.id)
        return render(request, 'esss/home/html', {"user":user1})
    except :
        return render(request, "esss/home.html")



def handlelogout(request):
    logout(request)
    messages.success(request,"Successfuly Logged  out" )
    return redirect('login')


def AllUserDetail(request):
    user=User.objects.all()
    return render(request, "esss/alluser.html", {"user":user})

class  AuthorUpdateView(View):
    def get(self,  request, myid):
        user=User.objects.all().get(id=myid)
        print(user)
        return render(request, 'esss/update.html', {"user": user})
    def post(self, request, myid):
        username1 = request.POST['username']
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email=request.POST['email']
        user=User.objects.all().get(id=myid)
        print(user.first_name)
        User.objects.filter(username=user.username).update(username=username1, first_name=first_name,last_name=last_name, email=email)
        return redirect('home')
@login_required(login_url='/login/')


def room(request, username):
    try :
        user1=request.user
        username1=User.objects.get(username=request.user)
        id=username1.id
        userdeitails = User.objects.all()
        return render(request, 'esss/index.html', {
            'room_name':"chatroom",
            'current_user_id': id,
            'user1':user1,
            'user3': userdeitails,
            })
    except:
        return render(request, 'esss/index.html')

@login_required(login_url='/login/')


def oneuserchat(request, username):
    try :
        user1=request.user
        username1=User.objects.get(username=request.user)
        id=username1.id
        userdeitails = User.objects.all()
        return render(request, 'esss/index.html', {
            'room_name':"chatroom",
            'current_user_id': id,
            'user1':user1,
            'user3': userdeitails,
            })
    except:
        return render(request, 'esss/index.html')

