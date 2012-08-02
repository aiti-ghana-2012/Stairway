
from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myhostels.views.home', name='home'),
    # url(r'^myhostels/', include('myhostels.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:

     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

<<<<<<< HEAD
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT,}),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),


    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT,}),





    url(r'^hostels/', include('hostels.urls')),
    url(r'^studentapp/', include('studentapp.urls')),
    url(r'^managerapp/', include('managerapp.urls')),
=======
>>>>>>> b29476a971a873791a4bf08e16ee917d4d290adf

    # Uncomment the next line to enable the admin:
      url(r'^admin/', include(admin.site.urls)),
      url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT,}),
      url(r'^hostels/', include('hostels.urls')),
      url(r'^managerapp/', include ('managerapp.urls')),
      url(r'^studentapp/', include ('studentapp.urls')),
      url(r'^media/(?P<path>.*)$','django.views.static.serve', {'document_root':settings.MEDIA_ROOT,}),
                       )
