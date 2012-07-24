from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

# Create your models here.

class Hostel(models.Model):
      location = models.TextField()
      manager = models.ForeignKey(User)
      hostel_name = models.CharField(max_length=30)
      website = models.URLField()
      def __unicode__(self):
        return self.hostel_name

class Institution(models.Model):
      institution_name = models.CharField(max_length=60)
      hostels = models.ManyToManyField(Hostel)
      city = models.CharField(max_length=60)
      location = models.TextField()
      website = models.URLField()
      def __unicode__(self):
       return self.institution_name

class Student(models.Model):
      GENDER_CHOICES = (('M','Male'),('F','Female'),)
      gender = models.CharField(max_length=1,choices=GENDER_CHOICES)
      id_number = models.CharField(max_length=60)
      user = models.ForeignKey(User, unique=True)
      phone_number = models.CharField(max_length=10)
      first_name = models.CharField(max_length=40)
      last_name = models.CharField(max_length=40)
      school = models.ForeignKey(Institution)
      program_of_study = models.CharField(max_length=60)
      email = models.EmailField()
      hostels = models.ManyToManyField(Hostel)
      address = models.TextField(max_length=50)
      LEVEL_IN_SCHOOL_CHOICES = (('100','Freshman'),('200','continuing'),('300','continuing'),('400','continuing'),('600','graduate'),)
      level = models.IntegerField(max_length=1,choices=LEVEL_IN_SCHOOL_CHOICES)
      def __unicode__(self):
       return self.id_number

class Rooms(models.Model):
      room_number = models.IntegerField()
      occupancy = models.IntegerField()
      space_available = models.IntegerField()
      hostels = models.ManyToManyField(Hostel)
      fee = models.DecimalField(max_digits=20, decimal_places=2)
      def __unicode__(self):
       return self.fee

class Reservation(models.Model):
      students = models.ManyToManyField(Student)
      hostel_name = models.ForeignKey(Hostel)
      occupancy = models.IntegerField()
      status = models.CharField(max_length=60)
      date_of_registration = models.DateField(auto_now_add=True)
      def __unicode__(self):
       return self.status

class Amenities(models.Model):
      name_of_amenities = models.CharField(max_length=60)
      status_of_amenities = models.CharField(max_length=60)
      room = models.ManyToManyField(Rooms)
      def __unicode__(self):
       return self.name_of_amenities


'''
admin.site.register(Hostel,HostelAdmin)
admin.site.register(Institution,InstitutionAdmin) 
admin.site.register(Student,StudentAdmin)
admin.site.register(Rooms,RoomsAdmin)
admin.site.register(Reservation,ReservationAdmin)
admin.site.register(Amenities,AmenitiesAdmin) 
'''
