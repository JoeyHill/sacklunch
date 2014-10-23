from django.conf.urls import patterns, include, url
from django.contrib import admin
from sacklunch.sandwich import views

admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^$', views.SandwichHome.as_view(), name='Sandwiches'),
    url(r'^create/(?P<orderid>[0-9]+)/$', views.SandwichForm.as_view(), name='Sandwich'), 
    )