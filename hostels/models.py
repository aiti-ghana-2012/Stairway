from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

# Create your models here.

class Hostel(models.Model):
      location = models.CharField(max_length = 255)
      manager = models.ForeignKey(User)
      manager_name = models.TextField()
      hostel_name = models.CharField(max_length = 255)
      #website = models.URLField()
      def __unicode__(self):
            return self.hostel_name

class Institution(models.Model):
      institution_name = models.CharField(max_length = 255)
      hostels = models.ForeignKey(Hostel)
      #city = models.CharField(max_length=60)
      location = models.TextField()
      #website = models.URLField()
      def __unicode__(self):
            return self.institution_name

class Student(models.Model):
      GENDER_CHOICES = (('M','Male'),('F','Female'),)
      gender = models.CharField(max_length=1,choices=GENDER_CHOICES)
      id_number = models.IntegerField()
      user = models.ForeignKey(User, unique=True)
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
      students = models.ManyToManyField(Student)
      hostels = models.ForeignKey(Hostel)
      occupancy = models.IntegerField()
      status = models.CharField(max_length=60)
      date_of_registration = models.DateField(auto_now_add=True)
      def __unicode__(self):
            return self.status

class Amenities(models.Model):
      name_of_amenities = models.CharField(max_length = 255)
      room = models.ManyToManyField(Rooms)
      def __unicode__(self):
            return self.name_of_amenities



admin.site.register(Hostel)
admin.site.register(Institution) 
admin.site.register(Student)
admin.site.register(Rooms)
admin.site.register(Reservation)
admin.site.register(Amenities) 
