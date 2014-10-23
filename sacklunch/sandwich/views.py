from django.shortcuts import render
from models import *
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
	class Meta:
		model = Sandwich
		fields = ['orderid', 'swbreadid', 'swmeatid', 'swcheeseid']

class SandwichToppingForms(forms.ModelForm):
	toppingid = forms.ModelMultipleChoiceField(queryset=Topping.objects.all(), label="Sandwich Topping", widget=forms.SelectMultiple(attrs={"style":"width:200px; height: 100px;"}))
	class Meta:
		model = SandwichTopping
		fields = ['toppingid']

SandwichFormSet = inlineformset_factory(Sandwich, SandwichTopping, form=SandwichToppingForms, extra=1)

class SandwichForm(LoggedInMixin, CreateView):
	template_name='sandwich/builder.html'
	form_class = SandwichBuilder
	model = Sandwich
	def get_initial(self):
		initials = super(SandwichForm, self).get_initial()
		initials['orderid'] = self.kwargs['orderid']
		return initials

	def get_context_data(self, **kwargs):
		context = super(SandwichForm, self).get_context_data(**kwargs)
		if self.request.POST:
			context['formset'] = SandwichFormSet(self.request.POST)
		else:
			context['formset'] = SandwichFormSet()
		return context

	def form_valid(self, form):
		context = self.get_context_data()
		formset = context['formset']
		if formset.is_valid():
			self.object = form.save(commit=False)
			formset.instance = self.object
			formset.save()

			return redirect(self.object.get_absolute_url())  # assuming your model has ``get_absolute_url`` defined.
		else:
			return self.render_to_response(self.get_context_data(form=form))