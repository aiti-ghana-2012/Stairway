
from django.contrib.auth.views import login, logout
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'managerapp.views.home'),
    url(r'^login/$', 'managerapp.views.do_login'),
    url(r'^logout/$', 'managerapp.views.do_logout'),
)
