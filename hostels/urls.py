
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'hostels.views.home'),
    url(r'^homepage/$', 'hostels.views.frontpage'),
<<<<<<< HEAD
    url(r'^homepage/(?P<id>\d+)/displayhostels$', 'hostels.views.hostels_list'),
   
    url(r'^homepage/gallery$','hostels.views.gallery'),
    url(r'^homepage/news$','hostels.views.news'),
    url(r'^homepage/about_us$','hostels.views.about_us'),
    url(r'^homepage/managerpage$', 'hostels.views.hostel_manager'),
    url(r'^homepage/managerpage/student/$','hostels.views.hostel_student'),
    url(r'^homepage/displayhostels/(?P<id>\d+)/((?P<hostelinfo>.*)/)?//$','hostels.views.hostels_detail'),
    url(r'^homepage/displayhostels/(?P<id>\d+)/((?P<hostelinfo>.*)/)?/studreg/$','hostels.views.studregister'),
    url(r'^homepage/student_confirmation/$','hostels.views.studconfirm'),

=======

    url(r'^homepage/(?P<id>\d+)/displayhostels/$', 'hostels.views.hostels_list'),
    url(r'^homepage/displayhostels/(?P<id>\d+)/$','hostels.views.hostels_detail'),
    url(r'^homepage/studentreg/$','hostels.views.studregister'),
    url(r'^homepage/roomreservation/$','hostels.views.roomreservation'),

    url(r'^homepage/news$','hostels.views.news'),
    url(r'^homepage/about_us$', 'hostels.views.about_us'),
    url(r'^homepage/terms$', 'hostels.views.terms'),

    url(r'^homepage/contact_us$', 'hostels.views.contact_us'),

    url(r'^homepage/faq$', 'hostels.views.faq'),


    url(r'^homepage/managerpage/$', 'hostels.views.hostel_manager'),
    #url(r'^homepage/managerpage/student/$','hostels.views.hostel_student'),
>>>>>>> b29476a971a873791a4bf08e16ee917d4d290adf

    #url(r'^hostel_manager_page/(?P<hostel_id>\d+)/$', 'hostels.views.hostel_manager'),
    url(r'^hostel_manager_page/$', 'hostels.views.hostel_manager'),
    #url(r'^hostel_manager_page/particular_student/$', 'hostels.views.hostel_student'),
    url(r'^homepage/student_confirmation/$','hostels.views.studconfirm')
)
