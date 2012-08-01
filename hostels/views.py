# Create your views here.
from django import forms
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
      password = forms.CharField(max_length=20)
      class Meta:
         
         model=Student
         exclude =('studuser',) 

@csrf_exempt
def studregister(request):
    form =RegistrationForm()    

    if request.method == 'POST':
	#student = Student()
        form = 	RegistrationForm(request.POST) # instance=student
        if form.is_valid():
  
            form.save()

        return HttpResponseRedirect(request.path)
    else:
       
        form = RegistrationForm()  
    my_context = Context({'form':form})
    return render_to_response('hostels/student_registration.html',my_context)



def roomreservation(request):
    roomdetails = Rooms.objects.all()
 
    my_context = Context({'reservation':roomdetails})    
    return render_to_response('hostels/room_reservation.html', my_context)


def about_us(request):
    return render_to_response('hostels/about_us.html', {})



def studconfirm(request):
    return render_to_response('hostels/student_confirmation.html',{})


def terms(request):
    return render_to_response('hostels/terms.html',{})



def news(request):
    return render_to_response('hostels/news.html',{})
def reserv(request):
    return render_to_response('hostels/reservation.html',{})

def hostel_manager(request):

    student_list = Student.objects.all()
    return render_to_response('hostels/hostel_manager_page.html', {'student_list':student_list})

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
>>>>>>> f14277aa2c63efe054f733fcf317efcce00d9271
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

    return render_to_response('hostels/particularstudent.html',{})



def home(request):
    return render_to_response('hostels/base.html',{})

