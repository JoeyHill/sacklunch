from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
import datetime
from sacklunch.order.forms import *
from sacklunch.order.models import *
from sacklunch.sandwich.models import *



# Create your views here.



from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from sacklunch.authUtils import LoggedInMixin
from django.views.generic import View




class OrderFormClass(forms.ModelForm):
    itementreeid = forms.ModelChoiceField(queryset=ItemEntree.objects.all(), widget=forms.Select(attrs={'onChange':'javascript:if(this.value == 1){alert("Sandwich")};'}), label="Choose your Entree:")
    itemdrinkid = forms.ModelChoiceField(queryset=ItemDrink.objects.all(), label="Choose your Drink:")
    itemsideid = forms.ModelChoiceField(queryset=ItemSide.objects.all(), label="Choose your Side:")
    itemfruitid = forms.ModelChoiceField(queryset=ItemFruit.objects.all(), label="Choose your Fruit:")
    class Meta:
        model = Order
        fields = ['itementreeid', 'itemdrinkid', 'itemsideid', 'itemfruitid', 'owner']

class OrderForm(LoggedInMixin, CreateView):
    template_name = 'order/orderBuilder.html'
    form_class = OrderFormClass
    model = Order
    success_url = '/order/list/'
    fields = ('itementreeid', 'itemdrinkid', 'itemsideid', 'itemfruitid', 'owner')
    def get_context_data(self, **kwargs):
        context = super(OrderForm, self).get_context_data(**kwargs)
        context['form'].fields['owner'].queryset = User.objects.filter(id=self.request.user.id)
        context['form'].fields['owner'].widget = forms.HiddenInput()
        return context
    def get_initial(self):
        initial = super(OrderForm, self).get_initial()
        initial = initial.copy()
        initial['owner'] = self.request.user.id
        return initial
    def get_success_url(self):
        request = self.request
        if request.method == "POST":
            if request.POST['itementreeid'] == '1':
                self.success_url = '/sandwich/create/'+str(self.object.orderid)
        return super(OrderForm, self).get_success_url()



class OrderList(LoggedInMixin, ListView):
    model = Order
    def get_queryset(self):
        return Order.objects.filter(owner=self.request.user)


class OrderDetail(LoggedInMixin, DetailView):
    model = Order

def order_view(request, orderid):
    order = Order.objects.get(orderid=orderid)
    context = {'order': order}
    return render(request, 'order/order_detail.html', context)




