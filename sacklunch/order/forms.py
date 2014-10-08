from sacklunch.item.models import Item
from django import forms
from django.forms import ModelForm
from sacklunch.order.models import Order

class OrderForm1(ModelForm):
	class Meta:
		model=Order

	def __init__(self, *args, **kwargs):
		super(OrderForm, self).__init__(*args, **kwargs)
		self.fields[''].queryset=()

class OrderForm(ModelForm):
	class Meta:
		model = Order