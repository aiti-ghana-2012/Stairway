# Create your views here.

from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.template import Context, loader
from django.http import HttpResponse
from django.contrib.auth.models import User
from models import Hostel,Institution,Student,Rooms,Reservation,Amenities 
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

   


def home(request):
    return render_to_response('hostels/base.html',{})

def about_us(request):
    return render_to_response('hostels/about_us.html', {})

def studregister(request,id,hostelinfo):
    return render_to_response('hostels/student_registration.html',{})


def studconfirm(request):
    return render_to_response('hostels/student_confirmation.html',{})


@csrf_exempt
def news(request):
    return render_to_response('hostels/news.html',{})
def reserv(request):
    return render_to_response('hostels/reservation.html',{})
@csrf_exempt
def hostel_manager(request):
    current_user = request.user
    if Student.objects.filter(user = current_user).count() is 1:
        return HttpResponseRedirect("/hostels/homepage/student_confirmation")
    else:
        thishostel = Hostel.objects.get(manager = current_user)
        student_list = thishostel.student_set.all()
        for std in student_list:
            astudent = Student.objects.get(id_number = std.id_number)
            room_number = Reservation.objects.get(students = astudent)
            if request.method == 'POST':
                currentid = request.POST['studentsearch']
                thisstudent= Student.objects.get(id_number = currentid)
                return render_to_response('hostels/particularstudent.html', {'everystudent':thisstudent, 'hostel_list':thishostel,'room_number':room_number})
            else:
                return render_to_response('hostels/hostel_manager_page.html', {'hostel_list':thishostel,'student_list':student_list,'room_number':room_number})
       
        
@csrf_exempt
def hostel_student(request):
    return render_to_response('hostels/particualrsturent.html',{})
        

 
