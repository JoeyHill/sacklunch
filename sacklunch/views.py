from django.views.generic.base import TemplateView
from django.template import RequestContext
from django.http import HttpResponse
from rest_framework import generics, permissions
from django.views.generic import ListView
from django.core.urlresolvers import reverse
from sacklunch.authUtils import LoggedInMixin
from django.shortcuts import redirect
import sacklunch

import pprint

class Home(TemplateView):
	template_name = 'home.html'
	
	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('/order/list/', permanent=True)
		return super(Home, self).dispatch(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super(Home, self).get_context_data(**kwargs)
		context['css'] = ['homepage']
		context['js'] = ['homepage']

		return context


def hello(request):
    return HttpResponse("Hello world")

from django.contrib.auth.models import User
from serializers import * 
from order.models import Order

def account_redirect(request):
	
	return redirect('/order/list/', permanent=True)

#class OrderList(generics.ListAPIView):
#    queryset = Order.objects.all()
#    serializer_class = OrderSerializer
#    permission_classes = [permissions.IsAuthenticated,]


