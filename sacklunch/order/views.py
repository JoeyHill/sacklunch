from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def createorder(request):
	now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def order_view(request):
     html = "<html><body>New View</body></html>"
     return HttpResponse(html)

def hello(request):
    return HttpResponse("Hello world")
