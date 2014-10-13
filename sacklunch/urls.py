#from django.conf.urls import patterns, include, url
from django.conf.urls import *
from django.contrib import admin
from django.contrib.auth.views import logout
from django.contrib.auth.views import login
from sacklunch import views
import sacklunch
from django.contrib.auth.decorators import login_required
admin.autodiscover()

#from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets, permissions, generics

from sacklunch.serializers import OrderViewSet, EntryViewSet, UserViewSet
from django.contrib.auth.models import User

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
from views import account_redirect


urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.Home.as_view(), name='home'),
    url(r'^login/$', login),
    url(r'^logout/$', logout),
    url(r'^order/', include('sacklunch.order.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^accounts/profile/$', account_redirect)
    
)
