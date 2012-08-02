# Create your views here.
from django import forms
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.template import Context, loader
from django.http import HttpResponse
<<<<<<< HEAD
from django import forms
from models import Hostel,Institution,Student,Rooms,Reservation,Amenities ,Confirmation
=======
from django.contrib.auth.models import User
from time import *
from models import Hostel,Institution,Student,Rooms,Reservation,Amenities 
>>>>>>> b29476a971a873791a4bf08e16ee917d4d290adf
from django.shortcuts import render_to_response
from django.contrib.admin import widgets  




def frontpage(request):
    Inst= Institution.objects.all()
<<<<<<< HEAD
=======
   
>>>>>>> c864b33b62d40ee1bce50001409770061a55b5e4
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

<<<<<<< HEAD
   

=======
>>>>>>> c864b33b62d40ee1bce50001409770061a55b5e4

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


class RegistrationForm(ModelForm):
      username = forms.CharField(max_length=20)
      password = forms.CharField(max_length=20)
      class Meta:
         
         model=Student
         exclude =('studuser',) 


def roomreservation(request):
    roomdetails = Rooms.objects.all()
 
    my_context = Context({'reservation':roomdetails})    
    return render_to_response('hostels/room_reservation.html', my_context)


def about_us(request):
    return render_to_response('hostels/about_us.html', {})

<<<<<<< HEAD
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
=======
def contact_us(request):
    return render_to_response('hostels/contact_us.html', {})

def faq(request):
    return render_to_response('hostels/faq.html', {})



def studconfirm(request):
    return render_to_response('hostels/student_confirmation.html',{})
>>>>>>> b29476a971a873791a4bf08e16ee917d4d290adf



def terms(request):
    return render_to_response('hostels/terms.html',{})


@csrf_exempt
def news(request):
    return render_to_response('hostels/news.html',{})
<<<<<<< HEAD
def reserv(request):
    return render_to_response('hostels/reservation.html',{})
@csrf_exempt
=======

>>>>>>> c864b33b62d40ee1bce50001409770061a55b5e4
def hostel_manager(request):

    student_list = Student.objects.all()
    return render_to_response('hostels/hostel_manager_page.html', {'student_list':student_list})

    current_user = request.user
    if Student.objects.filter(user = current_user).count() is 1:
        return HttpResponseRedirect("/hostels/homepage/student_confirmation")
    else:
        thishostel = Hostel.objects.get(manager = current_user)
        student_list = thishostel.student_set.all()
<<<<<<< HEAD
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
        

 
=======
        if request.method == 'POST':
           currentid = request.POST['studentsearch']
           thisstudent= Student.objects.get(id_number = currentid)
           return render_to_response('hostels/particularstudent.html', {'everystudent':thisstudent, 'hostel_list':thishostel})
        else:
            return render_to_response('hostels/hostel_manager_page.html', {'hostel_list':thishostel,'student_list':student_list})


    return render_to_response('hostels/particularstudent.html',{})
def about_us(request):
    return render_to_response('hostels/about_us.html',{})

def gallery(request):
    return render_to_response('hostels/gallery.html',{})

<<<<<<< HEAD
    
=======
def home(request):
    return render_to_response('hostels/base.html',{})

>>>>>>> b29476a971a873791a4bf08e16ee917d4d290adf
>>>>>>> c864b33b62d40ee1bce50001409770061a55b5e4
