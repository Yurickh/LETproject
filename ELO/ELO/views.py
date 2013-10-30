from django.shortcuts import render

from ELO.kernel.MainUnit import Factory

def index(request):
	return render(request, 'login/form.html', Factory().run())