
from django.contrib.auth.views import login, logout
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'studentapp.views.home'),
    url(r'^login/$', 'studentapp.views.do_login'),
    url(r'^logout/$', 'studentapp.views.do_logout'),
    url(r'^homepage/displayhostels/(?P<id>\d+)/((?P<hostelinfo>.*)/)?/studreg/$','hostels.views.studregister'),
    url(r'^homepage/displayhostels/(?P<id>\d+)/((?P<hostelinfo>.*)/)?/studreg/studcon$','hostels.views.studconfirm'),
)
