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


<<<<<<< HEAD
def hostels_detail(request,showparticularhostel):
    return render_to_response('hostels/hostels_detail.html',{})
=======


def hostels_detail(request,id):
    p = Hostel.objects.filter(hostel_name=id)
    q = Hostel.objects.get(id=id) 
    
    return render_to_response('hostels/hostels_detail.html', my_context)
    pass 

   
>>>>>>> b8513d67b0019e1ded237ab18b623d73d5a9f203

def home(request):
    return render_to_response('hostels/base.html',{})

def about_us(request):
    return render_to_response('hostels/about_us.html', {})

def studregister(request,id,hostelinfo):
    return render_to_response('hostels/student_registration.html',{})


def studconfirm(request):
    return render_to_response('hostels/student_confirmation.html',{})

<<<<<<< HEAD
@csrf_exempt
=======
def home(request):
    return render_to_response('hostels/base.html',{})

def news(request):
    return render_to_response('hostels/news.html',{})
def reserv(request):
    return render_to_response('hostels/reservation.html',{})


>>>>>>> b8513d67b0019e1ded237ab18b623d73d5a9f203
def hostel_manager(request):
    current_user = request.user
    if Student.objects.filter(user = current_user).count() is 1:
        return HttpResponseRedirect("/hostels/homepage/student_confirmation")
    else:
        thishostel = Hostel.objects.get(manager = current_user)
        student_list = thishostel.student_set.all()
        if request.method == 'POST':
           currentid = request.POST['studentsearch']
           thisstudent= Student.objects.get(id_number = currentid)
           return render_to_response('hostels/particularstudent.html', {'everystudent':thisstudent, 'hostel_list':thishostel})
        else:
            return render_to_response('hostels/hostel_manager_page.html', {'hostel_list':thishostel,'student_list':student_list})
        
"""@csrf_exempt
def hostel_student(request):
<<<<<<< HEAD
    current_user = request.user
    request.POST
    
    if Student.objects.filter(user = current_user).count() is 1:
        return HttpResponseRedirect("/hostels/homepage/student_confirmation")
    else:
        thishostel = Hostel.objects.get(manager = current_user)
        #student_list = thishostel.student_set.all()
        thisstudent= Student.objects.get(id_number = current_studentid)
        current_user = request.user
    user_list = User.objects.get(username = usename)
    user_id = user_list.id
    studentid = request.session['studentid']
    hostel_list = Hostel.objects.get(id = user_id)
    
    return render_to_response('hostels/particularstudent.html',{"hostel_list":thishostel, 'everystudent':thisstudent})"""
=======
    return render_to_response('hostels/particularstudent.html',{})
>>>>>>> b8513d67b0019e1ded237ab18b623d73d5a9f203

