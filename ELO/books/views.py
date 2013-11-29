from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from books.models import Publisher
from books.forms import ContactForm
from django import forms
from django.contrib.auth.forms import UserCreationForm

def search(request):
	errors = []
	if 'q' in request.GET:
		q = request.GET['q']
		if not q:
			errors.append('ENVIA ALGUMA COISA NEH ANIMAL')
		elif len(q) > 20:
			errors.append('MAIS DE 20 TA EXAGERANDO AE NEH CHAMPS')
		else:
			books = Publisher.objects.filter(name__icontains=q)
		 	return render(request, 'search_results.html',
				{'books': books, 'query': q})
	return render(request, 'search_form.html', {'errors': errors})

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			send_mail(
				cd['subject'], cd['message'], cd.get('email', 'noreply@example.com'),
				['donodosite@exemplo'],
			)
			return HttpResponseRedirect('/contact/thanks/')
	else:
		form = ContactForm(
			initial={'subject': 'Formulario SUPER legal!'}
		)
	return render(request, 'contact_form.html', {'form': form})

def brigado(request):
	return render(request, 'thanks.html');

def show_color(request):
    if "cor_favorita" in request.COOKIES:
        return HttpResponse("Sua cor favorita eh: %s" % \
            request.COOKIES["cor_favorita"])
    else:
        return HttpResponse("Voce nao tem uma cor favorita")

def set_color(request):
	if "cor_favorita" in request.GET:

		response = HttpResponse("Sua cor favorita eh agora: %s" % request.GET["cor_favorita"])
		response.set_cookie("cor_favorita", request.GET["cor_favorita"])

		return response
	else:
		return HttpResponse("You didn't give a favorite color")

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			return HttpResponseRedirect("/books/")
	else:
		form = UserCreationForm()
	return render(request, "register.html", {'form': form,})
