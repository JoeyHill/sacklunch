from django.conf.urls import patterns, include, url
from sacklunch import *
from sacklunch import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sacklunch.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.Home.as_view(), name='home'),
    # url(r'^order/',include('sacklunch.order.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
