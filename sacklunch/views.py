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

def user_exists(username):
	if User.objects.filter(username=username).count():
		return True
	return False


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
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth import login
import datetime

class UserForm(forms.ModelForm):
	def clean_password(self):
		username = self.cleaned_data['username']
		pword = self.cleaned_data['password']
		user = self.save(commit=False)
		#hashes the password
		user.set_password(pword)
		password = user.password
		existing = user_exists(username)
		userobject = authenticate(username=username, password=password)
		if existing:
			if userobject is None:
				raise forms.ValidationError('But the credentials supplied are incorrect.')

			else:
				data = user.password
		else:
			data = user.password
			user.save()
		return data


		#if user_exists(uname):
			#response = urllib.urlopen('http://tropicanagardens.com/it/test.html')
			#result = response.read()
			#login(req, self.get_user())
			#return HttpResponseRedirect('/order/list/')
			#raise forms.ValidationError(result)

		# Always return the cleaned data, whether you have changed it or
		# not.
			
	class Meta:
		model = User
		fields = ('username', 'password')
		widgets = {
            'password': forms.PasswordInput(),
        }

from django.contrib.auth import authenticate, login, logout
class AddUser(CreateView):
	template_name = "auth/user_form.html"
	form_class = UserForm
	success_url = '/order/list/'
	#Form Valid Override	
	#Auto Login for Successful Registration
	def get_success_url(self):
		request = self.request
		user = authenticate(username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			if user.is_active:
				login(request, user)
				redirect('/order/list/')
		return super(AddUser, self).get_success_url()
	#prevent save if user exists, try login
	def post(self, request, *args, **kwargs):
		username = request.POST['username']
		password = request.POST['password']
		if user_exists(username):
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request,user)
					return HttpResponseRedirect('/order/list/')
		return super(AddUser, self).post(self, request, *args, **kwargs)


		



#class OrderList(generics.ListAPIView):
#    queryset = Order.objects.all()
#    serializer_class = OrderSerializer
#    permission_classes = [permissions.IsAuthenticated,]



