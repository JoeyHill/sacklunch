from django.conf.urls import patterns, include, url
from django.contrib import admin
from sacklunch.order import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sacklunch.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$','',name='createorder')),
    # url(r'^$',hello)
    url(r'^create/$',views.createRelationOrder, name='newOrder'),
)