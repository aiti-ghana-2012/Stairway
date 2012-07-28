# Create your views here.
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.template import Context, loader
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.db import models
from hostels.models import Hostel,Institution,Student,Rooms,Reservation,Amenities 
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

@csrf_exempt
def do_login(request):
    if request.method == 'POST':
        #YOUR CODE HERE
       uname = request.POST['username'
]   # user's username is kept in a dictionary
       passwd = request.POST['password']  # user's password is kept in a dictionary
       
       
       user = authenticate(username=uname, password=passwd)
       
       if user is not None and user.is_active:
       	   
    	   login(request, user) 
           current_user = request.user
    	   if Hostel.objects.filter(manager = current_user).count() is 1:
               return HttpResponseRedirect("/hostels/hostel_manager_page")
           elif Student.objects.filter(user = current_user).count() is 1:
               return HttpResponseRedirect("/hostels/homepage/student_confirmation")
           else:
               return HttpResponse("invalid username and password!!!")
       else:
            return HttpResponse("wrong Username or password. User Authentication failed!!!")
              
                 
  

    form = LoginForm()
    return render_to_response('managerapp/login.html', {
        'form': form,
        'logged_in': request.user.is_authenticated()
    })

@csrf_exempt
def do_logout(request):
    logout(request)
    return render_to_response('managerapp/logout.html')

def home(request):
     return render_to_response('hostels/base.html',{})

