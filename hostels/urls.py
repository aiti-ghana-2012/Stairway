
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'hostels.views.home'),
    url(r'^homepage/$', 'hostels.views.frontpage'),
<<<<<<< HEAD
    url(r'^homepage/displayhostels$', 'hostels.views.hostels_list'),
    url(r'^homepage/displayhostels/((?P<showparticularhostel>.*)/)?$','hostels.views.hostels_detail'),
    #url(r'^homepage/displayhostels/(?P<id>\d+)/((?P<hostelinfo>.*)/)?//$','hostels.views.hostels_detail'),
=======
    url(r'^homepage/(?P<id>\d+)/displayhostels/$', 'hostels.views.hostels_list'),
    url(r'^homepage/displayhostels/(?P<id>\d+)/$','hostels.views.hostels_detail'),
    #url(r'^homepage/displayhostels/(?P<id>\d+)/((?P<hostelinfo>.*)/)?/studreg/$','hostels.views.studregister'),
    #url(r'^homepage/displayhostels/(?P<id>\d+)/((?P<hostelinfo>.*)/)?/studreg/studcon$','hostels.views.studconfirm'),


    url(r'^homepage/news$','hostels.views.news'),

    url(r'^homepage/managerpage/$', 'hostels.views.hostel_manager'),
    url(r'^homepage/managerpage/student/$','hostels.views.hostel_student'),
>>>>>>> b8513d67b0019e1ded237ab18b623d73d5a9f203

    url(r'^homepage/aboutus$', 'hostels.views.about_us'),
    #url(r'^hostel_manager_page/(?P<hostel_id>\d+)/$', 'hostels.views.hostel_manager'),
    url(r'^hostel_manager_page/$', 'hostels.views.hostel_manager'),
    url(r'^hostel_manager_page/particular_student/$', 'hostels.views.hostel_student'),
    url(r'^homepage/student_confirmation/$','hostels.views.studconfirm')
)
