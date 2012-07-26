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
<<<<<<< HEAD
<<<<<<< HEAD
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
=======
<<<<<<< HEAD
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT,}),
=======
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
>>>>>>> 0bb5324c943e8a895b2e4e224d393b2d7f8a393e
>>>>>>> 474d9e8cb47bb0cb36a741528c55ac6ee76b7706
=======
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
      url(r'^admin/', include(admin.site.urls)),
      url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT,}),
      url(r'^hostels/', include('hostels.urls')),
>>>>>>> c97d1ef9ea01d8b0c0b242ae3e03cf5fcf857a92
)
