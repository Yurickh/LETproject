from django.http import HttpResponse

from ELO.kernel.MainUnit import Factory

def index(request):
	return HttpResponse(Factory().run())