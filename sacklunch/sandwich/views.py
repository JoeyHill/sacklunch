from django.shortcuts import render
from models import *
from sacklunch.order.models import Order
from django import forms
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from sacklunch.authUtils import LoggedInMixin
from django.views.generic import View
from django.forms.models import inlineformset_factory
# Create your views here.

class SandwichBuilder(forms.ModelForm):
	orderid = forms.CharField(max_length=100, widget=forms.HiddenInput())
	swbreadid = forms.ModelChoiceField(queryset=swBread.objects.all(), label="What kind of bread?")
	swmeatid = forms.ModelChoiceField(queryset=swMeat.objects.all(), label="What kind of meat?")
	swcheeseid = forms.ModelChoiceField(queryset=swCheese.objects.all(), label="What kind of cheese?")
	toppings = forms.ModelMultipleChoiceField(queryset=Topping.objects.all(), label='Select your toppings', widget=forms.SelectMultiple(attrs={"style":"width:200px; height: 100px;"}))
	class Meta:
		model = Sandwich
		fields = ['orderid', 'swbreadid', 'swmeatid', 'swcheeseid']

class SandwichToppingForms(forms.ModelForm):
	toppingid = forms.ModelMultipleChoiceField(queryset=Topping.objects.all(), label="Sandwich Topping", widget=forms.SelectMultiple(attrs={"style":"width:200px; height: 100px;"}))
	class Meta:
		model = SandwichTopping
		fields = ['toppingid']

#SandwichFormSet = inlineformset_factory(Sandwich, SandwichTopping, form=SandwichToppingForms, extra=1)

class SandwichForm(LoggedInMixin, CreateView):
	template_name='sandwich/builder.html'
	form_class = SandwichBuilder
	model = Sandwich
	success_url = '/order/list/'
	def get_initial(self):
		initials = super(SandwichForm, self).get_initial()
		initials['orderid'] = self.kwargs['orderid']
		return initials

	def form_valid(self, form):
		sw = form.save()
		sw.orderid = self.request.POST['orderid']
		sw.save()
		order = Order.objects.get(orderid=sw.orderid)
		order.sandwichid = sw
		order.save()
		for topping in self.request.POST.getlist('toppings'):
			toppings = SandwichTopping.objects.create(sandwichid=sw , toppingid=Topping.objects.get(toppingid=topping))
		return super(SandwichForm, self).form_valid(form)

