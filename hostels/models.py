
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

# Create your models here.

            
class Institution(models.Model):
      institution_name = models.CharField(max_length = 255)
      location = models.TextField()
      def __unicode__(self):
            return self.institution_name
      def get_absolute_url(self):
       return "/hostels/homepage/%i/displayhostels" % self.id
      
class Hostel(models.Model):
      location = models.CharField(max_length = 255)
      manager = models.OneToOneField(User)
      manager_name = models.TextField()
      hostel_name = models.CharField(max_length = 255)
      institutions = models.ForeignKey(Institution)
      #user = models.ForeignKey(User, unique = True)
      #myuser.groups = (manager)
      #room=models.ForeignKey(Rooms)
      #website = models.URLField()
      def __unicode__(self):
            return str(self.hostel_name)
      def get_absolute_url(self):
            return "/hostels/homepage/displayhostels/%i" % self.id

       
"""hostel_name = models.CharField(max_length = 255)
      hostel_description = models.TextField()
      manager = models.ForeignKey(User)  #the manager here is the database user
      hostel_manager_name = models.CharField(max_length= 255)
      institution = models.ForeignKey(Institution)
      def __unicode__(self):
            return self.hostel_name"""     

class Student(models.Model):
      GENDER_CHOICES = (('Male','Male'),('Female','Female'),)
      gender = models.CharField(max_length=10,choices=GENDER_CHOICES)
      id_number = models.IntegerField()
      user = models.OneToOneField(User, unique=True)
      phone_number = models.IntegerField(max_length=10)
      first_name = models.CharField(max_length = 255)
      last_name = models.CharField(max_length = 255)
      school = models.ForeignKey(Institution)
      program_of_study = models.CharField(max_length = 255)
      email = models.EmailField()
      hostels = models.ForeignKey(Hostel)
      LEVEL_IN_SCHOOL_CHOICES= (('100','100'), ('200','200'), ('300','300'), ('400','400'))
      level = models.CharField(max_length = 4, choices = LEVEL_IN_SCHOOL_CHOICES)
      picture = models.ImageField(upload_to = 'uploaded_images/')
      def __unicode__(self):
            return str(self.id_number)

class Rooms(models.Model):
      room_number = models.CharField(max_length=60)
      OCCUPANCY_CHOICES =(('1 in a room','1 in a room'),('2 in a room','2 in a room'),('4 in a room','4 in a room'))
      occupancy = models.CharField(max_length=100,choices=OCCUPANCY_CHOICES)
      space_available = models.IntegerField()
      hostel= models.ManyToManyField(Hostel)
      fee = models.DecimalField(max_digits=20, decimal_places=2)
      def __unicode__(self):
            return str(self.occupancy)

class Reservation(models.Model):
      students = models.OneToOneField(Student)
      hostels = models.ForeignKey(Hostel)
      occupancy = models.ForeignKey(Rooms)
      STATUS_CHOICES =(('reserved','reserved'),('not_reserved','not_reserved'))
      status = models.CharField(max_length=60,choices=STATUS_CHOICES)
      date_of_registration = models.DateField(auto_now_add=True)
      room_num = models.IntegerField()
      reciept = models.CharField(max_length = 255)
      def __unicode__(self):
            return self.status

class Amenities(models.Model):
      name_of_amenities = models.CharField(max_length = 255)
      room = models.ManyToManyField(Rooms)
      def __unicode__(self):
            return self.name_of_amenities

class HostelAdmin(admin.ModelAdmin):

    list_display=('hostel_name','manager_name','location','institutions')
    search_fields =('hostel_name','location')
    list_filter =('hostel_name',)

    #inlines=[InstitutionInline]

class InstitutionAdmin(admin.ModelAdmin):
    list_display=('institution_name','location')
    search_fields =('institution_name','hostels','location')
    list_filter =('institution_name',)

class StudentAdmin(admin.ModelAdmin):
    list_display=('gender','id_number','phone_number','first_name','last_name','program_of_study')
    search_fields =('id_number','last_name','first_name')
    list_filter =('id_number',)
    
class ReservationAdmin(admin.ModelAdmin):
    list_display=('status','date_of_registration')
    search_fields =('students',)
    list_filter=('students',)

class InstitutionInline(admin.TabularInline):
    model=Institution     
    


admin.site.register(Hostel,HostelAdmin)
admin.site.register(Institution,InstitutionAdmin) 
admin.site.register(Student,StudentAdmin)
admin.site.register(Reservation,ReservationAdmin)
admin.site.register(Amenities)
admin.site.register(Rooms) 


