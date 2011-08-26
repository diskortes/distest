from django.conf.urls.defaults import patterns, include, url
from distest.main.views import show_mydata, show_META

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'distest.views.home', name='home'),
    # url(r'^distest/', include('distest.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', show_mydata),
    url(r'^meta/$', show_META)
)
