"""
This code should be copy and pasted into blog/urls.py
"""
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'hostels.views.home'),
    url(r'^homepage/$', 'hostels.views.frontpage'),
    url(r'^homepage/displayhostels$', 'hostels.views.hostels_list'),
    url(r'^homepage/displayhostels/(?P<id>\d+)/((?P<showparticularhostel>.*)/)?$','hostels.views.hostels_detail'),
    
    
)

