#from django.conf.urls import patterns, include, url
from django.conf.urls import *
from django.contrib import admin
from sacklunch import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.Home.as_view(), name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$', views.Home.as_view(), name='home'),
    url(r'^order/', include('sacklunch.order.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^order/app/','order.views.hello'),
)
