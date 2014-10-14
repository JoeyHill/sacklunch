from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
import datetime
from sacklunch.order.forms import *
from sacklunch.order.models import *



# Create your views here.



from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from sacklunch.authUtils import LoggedInMixin
from django.views.generic import View



class OrderForm(LoggedInMixin, CreateView):
    template_name = 'formTemplate.html'
    model = Order
    success_url = '/orderlist/'
    fields = ('itementreeid', 'itemdrinkid', 'itemsideid', 'itemfruitid', 'owner')
    def get_context_data(self, **kwargs):
        context = super(OrderForm, self).get_context_data(**kwargs)
        context['form'].fields['owner'].queryset = User.objects.filter(id=self.request.user.id)
        return context
    def get_initial(self):
        initial = super(OrderForm, self).get_initial()
        initial = initial.copy()
        initial['owner'] = self.request.user.id
        return initial


class OrderList(LoggedInMixin, ListView):
    model = Order
    def get_queryset(self):
        return Order.objects.filter(owner=self.request.user)


class OrderDetail(LoggedInMixin, DetailView):
    model = Order


    

