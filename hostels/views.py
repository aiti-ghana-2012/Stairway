# Create your views here.
from django import forms
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.template import Context, loader
from django.http import HttpResponse
from django.contrib.auth.models import User
from time import *

from models import Hostel,Institution,Student,Rooms,Reservation,Amenities 
from django.shortcuts import render_to_response
from django.contrib.admin import widgets  

def frontpage(request):
    Inst= Institution.objects.all()
    
    my_context = Context({'allinstitutions':Inst})   
    return render_to_response ('hostels/frontpage.html', my_context)
    
def hostels_list(request,id):
    bla = Hostel.objects.filter(institution=id) #gets the institution attribute of the Hostel class 
    institute = Institution.objects.get(id=id)  #gets the id of the Institution class
    description = Institution.objects.filter(id=id)
    my_context = Context({'allhostels':bla,'institution':institute,'description':description})   
    return render_to_response ('hostels/hostels_list.html', my_context)


def hostels_detail(request,id):
    amenities=[]
    ''' q = Hostel.objects.get(id=id) 
    amenities = Amenities.objects.filter(room__hostel=id) #if room is an attribute to Amenities
    my_context = Context({'hostel':q,'amenities':amenities})    
    return render_to_response('hostels/hostels_detail.html', my_context)
    '''   
    q = Hostel.objects.get(id=id)
    allhostels = Hostel.objects.filter(id=id) 
    hostelfee = Rooms.objects.filter(fee=id)  
    all_amenities = Amenities.objects.all()
    for a in all_amenities:
        if a.rooms_set.filter(hostel=id):
            amenities.append(a)
    my_context = Context({'hostel':q,'amenities':amenities,'allhostels':allhostels,'hostelfee':hostelfee})    
    return render_to_response('hostels/hostels_detail.html', my_context)


class RegistrationForm(ModelForm):
      username = forms.CharField(max_length=20)
      password = forms.CharField(widget=forms.PasswordInput())
      confirm_password = forms.CharField(widget=forms.PasswordInput()) 
      date_of_birth = forms.DateField(widget=forms.DateInput(format = '%d-%m-%Y'), input_formats=('%d-%m-%Y',), initial = "DD-MM-YYYY")
      class Meta:
         
         model=Student
         #widgets = {'password':forms.PasswordInput(),}
         exclude =('studuser',) 


@csrf_exempt
def studregister(request):
    #form =RegistrationForm()    

    if request.method == 'POST':
	student = Student(studuser = User.objects.create_user(request.POST["username"], request.POST["email"], request.POST["password"]))
      	print "User submitted data"
	form = 	RegistrationForm(request.POST, instance=student) 
	print request.POST["username"], request.POST["email"], request.POST["password"]
        
        if form.is_valid():
            print "It validated"
            form.save()
	else:
	    print "It didnt validate"
        my_context = Context({'form':form})
        return render_to_response('hostels/student_registration.html',my_context)
        return HttpResponseRedirect(request.path)
    else:
	print "It's not post"
       
        form = RegistrationForm()  
    my_context = Context({'form':form})
    return render_to_response('hostels/student_registration.html',my_context)



def roomreservation(request):
    roomdetails = Rooms.objects.all()
 
    my_context = Context({'reservation':roomdetails})    
    return render_to_response('hostels/room_reservation.html', my_context)




def studconfirm(request,id,hostelinfo):
    return render_to_response('hostels/student_confirmation.html',{})

def about_us(request):
    return render_to_response('hostels/about_us.html',{})

def terms(request):
    return render_to_response('hostels/terms.html',{})

def news(request):
    return render_to_response('hostels/news.html',{})


def hostel_manager(request):
    student_list = Student.objects.all()
    return render_to_response('hostels/hostel_manager_page.html', {'student_list':student_list})


def hostel_student(request):
    return render_to_response('hostels/particularstudent.html',{})


def home(request):
    return render_to_response('hostels/base.html',{})

