from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.template import Context, loader
from django.http import HttpResponse

from models import Hostel,Institution,Student,Rooms,Reservation,Amenities, 
from django.shortcuts import render_to_response
class StudentForm(ModelForm):
    class Meta:
    model=Student
@csrf_exempt
def student_registration(request):
if request.method=="POST":
form=StudentForm(request.POST)
if form.is_valid():
return HttpResponse()
else:
form=StudentForm()
return render_to_response('student_registration.html',{'form':form,})
   
    
