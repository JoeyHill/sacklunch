#from django.conf.urls import patterns, include, url
from django.conf.urls import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sacklunch.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$', views.Home.as_view(), name='home'),
    url(r'^order/', 'sacklunch.views.hello'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^order/app/','order.views.hello'),
)
