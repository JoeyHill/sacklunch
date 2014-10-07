from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
import datetime
from sacklunch.order.models import *
from django.forms.models import inlineformset_factory

# Create your views here.
def createorder(request):
	if request.method == "POST":
		form = OrderForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/thanks/')
	else:
		form = OrderForm()

	return render(request, 'formTemplate.html', {'form': form})

def createRelationOrder(request):
    order=Order.objects.get(pk=3)
    OrderInlineFormSet = inlineformset_factory(Order, OrderItems)
    if request.method == "POST":
        formset = OrderInlineFormSet(request.POST, request.FILES, instance=order)
        if formset.is_valid():
            formset.save()
            # Do something. Should generally end with a redirect. For example:
            return HttpResponseRedirect(order.get_absolute_url())
    else:
        formset = OrderInlineFormSet(instance=order)
    return render_to_response("formTemplate.html", {
        "formset": formset,
    })

def order_view(request):
     html = "<html><body>New View</body></html>"
     return HttpResponse(html)

def hello(request):
    return HttpResponse("Hello world")
