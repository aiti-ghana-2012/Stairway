# Create your views here.
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.template import Context, loader
from django.http import HttpResponse

from models import Hostel,Institution,Student,Rooms,Reservation,Amenities 
from django.shortcuts import render_to_response

def frontpage(request):
    return render_to_response('hostels/frontpage.html',{})

def hostels_list(request):
    pass

def hostels_detail(request,id,showparticularhostel):
    return render_to_response('hostels/display_particular_hostel.html', {} )




def home(request):
    return render_to_response('hostels/base.html',{})
def hostel_manager(request):
    student_list = Student.objects.all()
    return render_to_response('hostels/hostel_manager_page.html', {'student_list':student_list})
def hostel_student(request):
    return render_to_response('hostels/particularstudent.html',{})
