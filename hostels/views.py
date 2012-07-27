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
    return render_to_response('hostels/hostels_list.html',{})

def AMENhostels_detail(request,id,hostelinfo):
    return render_to_response('hostels/AMENhostels_detail.html',{})


def BRUNEIhostels_detail(request,id,hostelinfo):
    return render_to_response('hostels/BRUNEIhostels_detail.html',{})

def studregister(request,id,hostelinfo):
    return render_to_response('hostels/student_registration.html',{})

def studconfirm(request,id,hostelinfo):
    return render_to_response('hostels/student_confirmation.html',{})
def home(request):
    return render_to_response('hostels/base.html',{})
