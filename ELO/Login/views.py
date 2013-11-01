from django.shortcuts import render
from django.http import HttpResponseRedirect

from ELO.MainUnit import Factory

from forms import LoginForm

def loginScreen(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			try:
				Factory.run()
			except exc:
				return render(request, 'login/form.html', {'form': LoginForm(), 'errors': exc,})
			return HttpResponseRedirect('/home/')
	else:
		return render(request, 'login/form.html', {'form': LoginForm()})

def logoutScreen(request): pass