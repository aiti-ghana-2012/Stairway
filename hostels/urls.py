
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'hostels.views.home'),
    url(r'^homepage/$', 'hostels.views.frontpage'),
    url(r'^homepage/(?P<id>\d+)/displayhostels/$', 'hostels.views.hostels_list'),
    url(r'^homepage/displayhostels/(?P<id>\d+)/$','hostels.views.hostels_detail'),
    #url(r'^homepage/displayhostels/(?P<id>\d+)/((?P<hostelinfo>.*)/)?/studreg/$','hostels.views.studregister'),
    #url(r'^homepage/displayhostels/(?P<id>\d+)/((?P<hostelinfo>.*)/)?/studreg/studcon$','hostels.views.studconfirm'),


    url(r'^homepage/news$','hostels.views.news'),

    url(r'^homepage/managerpage/$', 'hostels.views.hostel_manager'),
    url(r'^homepage/managerpage/student/$','hostels.views.hostel_student'),

    
)
