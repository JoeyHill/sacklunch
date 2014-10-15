from django.views.generic.base import TemplateView
from django.template import RequestContext
from django.http import HttpResponse
from rest_framework import generics, permissions
from django.views.generic import ListView, CreateView
from django.core.urlresolvers import reverse
from sacklunch.authUtils import LoggedInMixin
from django.shortcuts import redirect
import sacklunch
from sacklunch.entry.models import Entry

import urllib
from django.core.exceptions import ValidationError

import pprint

class Home(TemplateView):
	template_name = 'home.html'
	
	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('/order/list/')
		return super(Home, self).dispatch(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super(Home, self).get_context_data(**kwargs)
		context['css'] = ['homepage']
		context['js'] = ['homepage']

		return context


def hello(request):
    return HttpResponse("Hello world")

from django.contrib.auth.models import User

def account_redirect(request):
	
	return redirect('/order/list/', permanent=True)


from django import forms

class UserForm(forms.ModelForm):
	def clean_username(self):
		data = self.cleaned_data['username'] 
		if True:
			raise forms.ValidationError("You have forgotten about Fred!")

		# Always return the cleaned data, whether you have changed it or
		# not.
		return data
	class Meta:
		model = User
		fields = ('username', 'password')

class AddUser(CreateView):
	template_name = "auth/user_form.html"
	form_class = UserForm
	


		



#class OrderList(generics.ListAPIView):
#    queryset = Order.objects.all()
#    serializer_class = OrderSerializer
#    permission_classes = [permissions.IsAuthenticated,]


