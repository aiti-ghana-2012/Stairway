
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'hostels.views.home'),
    url(r'^homepage/$', 'hostels.views.frontpage'),
    url(r'^homepage/displayhostels$', 'hostels.views.hostels_list'),
    url(r'^homepage/displayhostels/(?P<id>\d+)/((?P<showparticularhostel>.*)/)?$','hostels.views.hostels_detail'),
    url(r'^homepage/managerpage/$', 'hostels.views.hostel_manager'),
    url(r'^homepage/managerpage/student/$','hostels.views.hostel_student'),
    url(r'^homepage/displayhostels/(?P<id>\d+)/((?P<hostelinfo>.*)/)?//$','hostels.views.hostels_detail'),
    url(r'^homepage/displayhostels/(?P<id>\d+)/((?P<hostelinfo>.*)/)?/studreg/$','hostels.views.studregister'),
    url(r'^homepage/displayhostels/(?P<id>\d+)/((?P<hostelinfo>.*)/)?/studreg/studcon$','hostels.views.studconfirm'),

    
)
