# Create your views here.

from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.template import Context, loader
from django.http import HttpResponse
from django import forms
from models import Hostel,Institution,Student,Rooms,Reservation,Amenities ,Confirmation
from django.shortcuts import render_to_response




def frontpage(request):
    Inst= Institution.objects.all()
    
    my_context = Context({'allinstitutions':Inst})   
    return render_to_response ('hostels/frontpage.html', my_context)
    
def hostels_list(request,id):
    bla = Hostel.objects.filter(institution=id)
    institute = Institution.objects.get(id=id)
    my_context = Context({'allhostels':bla,'institution':institute})   
    return render_to_response ('hostels/hostels_list.html', my_context)




def hostels_detail(request,id):
    p = Hostel.objects.filter(hostel_name=id)
    q = Hostel.objects.get(id=id) 
    
    return render_to_response('hostels/hostels_detail.html', my_context)
    pass 

   


def studregister(request,id,hostelinfo):
    return render_to_response('hostels/student_registration.html',{})


class ConfirmationForm(ModelForm):
      class Meta:
            model=Confirmation
            exclude=["con"]

@csrf_exempt
def studconfirm(request):
    currentuser = request.user
    std= Student.objects.get(user = currentuser)
    stuhostel=std.hostels
    hos=Hostel.objects.get(id=stuhostel.id)
    form=ConfirmationForm()
    message=""
    thisstudent=Student.objects.get(user=currentuser)
    status=False
    if request.method=="POST":
        userinstance=Confirmation(con=thisstudent)
        form=ConfirmationForm(request.POST,instance=userinstance)
        
        if form.is_valid():
            status=True
            message="Thank You"
            form.save()
        return render_to_response('hostels/student_confirmation.html',locals())
        
    return render_to_response('hostels/student_confirmation.html',locals())

def home(request):
    return render_to_response('hostels/base.html',{})

def news(request):
    return render_to_response('hostels/news.html',{})


def hostel_manager(request):
    student_list = Student.objects.all()
    return render_to_response('hostels/hostel_manager_page.html', {'student_list':student_list})
def hostel_student(request):
    return render_to_response('hostels/particularstudent.html',{})
def about_us(request):
    return render_to_response('hostels/about_us.html',{})

def gallery(request):
    return render_to_response('hostels/gallery.html',{})

    
