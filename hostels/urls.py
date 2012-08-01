
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'hostels.views.home'),
    url(r'^homepage/$', 'hostels.views.frontpage'),
    url(r'^homepage/(?P<id>\d+)/displayhostels/$', 'hostels.views.hostels_list'),
    url(r'^homepage/displayhostels/(?P<id>\d+)/$','hostels.views.hostels_detail'),
    url(r'^homepage/studentreg/$','hostels.views.studregister'),
    url(r'^homepage/roomreservation/$','hostels.views.roomreservation'),


    url(r'^homepage/news$','hostels.views.news'),
    url(r'^homepage/about_us$', 'hostels.views.about_us'),
    url(r'^homepage/terms$', 'hostels.views.terms'),

    url(r'^homepage/managerpage/$', 'hostels.views.hostel_manager'),
    url(r'^homepage/managerpage/student/$','hostels.views.hostel_student'),

    
)
