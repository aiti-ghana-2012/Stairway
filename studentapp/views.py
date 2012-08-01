# Create your views here.

from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.template import Context, loader
from hostels.models import Hostel, Student

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

@csrf_exempt
def do_login(request):
    if request.method == 'POST':
        #YOUR CODE HERE
       uname = request.POST['username']   # user's username is kept in a dictionary
       passwd = request.POST['password']  # user's password is kept in a dictionary
       user = authenticate(username=uname, password=passwd)
       if user is not None and user.is_active:
       	   
    	   login(request, user)  # redirect user to a success page
    	   currentuser = request.user
    	   if Student.objects.filter(user = currentuser).count() is 1:
               return HttpResponseRedirect("/hostels/homepage/student_confirmation/")
           elif Hostel.objects.filter(manager =currentuser).count() is 1:
                return HttpResponseRedirect("/hostels/hostel_manager_page")
           else:
                return HttpResponseRedirect ("invalid username and password")
       else:
           return HttpResponse("wrong Username or password. User Authentication failed!!!") 
        

           
              
  

    form = LoginForm()
    return render_to_response('studentapp/login.html', {
        'form': form,
        'logged_in': request.user.is_authenticated()
    })

@csrf_exempt
def do_logout(request):
    logout(request)
    return render_to_response('studentapp/logout.html')

def home(request):
     return render_to_response('hostels/base.html',{})
