from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

# Create your models here.

class Hostel(models.Model):
      location = models.CharField(max_length = 255)
      manager = models.OneToOneField(User)
      manager_name = models.TextField()
      hostel_name = models.CharField(max_length = 255)
      #user = models.ForeignKey(User, unique = True)
     #myuser.groups = (manager)
      #room=models.ForeignKey(Rooms)
      #website = models.URLField()
      def __unicode__(self):
            return str(self.hostel_name)

class Institution(models.Model):
      institution_name = models.CharField(max_length = 255)
      hostels = models.ForeignKey(Hostel)
      #city = models.CharField(max_length=60)
      location = models.TextField()
      #website = models.URLField()
      def __unicode__(self):
            return self.institution_name

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
      picture = models.ImageField(upload_to = 'images/uploads/')
      def __unicode__(self):
            return str(self.id_number)

class Rooms(models.Model):
      room_number = models.IntegerField()
      occupancy = models.IntegerField()
      space_available = models.IntegerField()
      hostel= models.ManyToManyField(Hostel)
      fee = models.DecimalField(max_digits=20, decimal_places=2)
      def __unicode__(self):
            return self.fee

class Reservation(models.Model):
      students = models.OneToOneField(Student)
      hostels = models.ForeignKey(Hostel)
      occupancy = models.IntegerField()
      status = models.CharField(max_length=60)
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
    list_display=('manager','location')
    search_fields =('hostel_name','location')
    list_filter =('location',)
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


