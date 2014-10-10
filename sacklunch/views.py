from django.views.generic.base import TemplateView
from django.template import RequestContext
from django.http import HttpResponse

import pprint

class Home(TemplateView):
	template_name = 'home.html'
	def get_context_data(self, **kwargs):
		context = super(Home, self).get_context_data(**kwargs)
		context['css'] = ['homepage']
		context['js'] = ['homepage']

		return context


def hello(request):
    return HttpResponse("Hello world")

