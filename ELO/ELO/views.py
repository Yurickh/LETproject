from django.http import HttpResponse

def main(request):
	return HttpResponse()

def hello(request):
	return HttpResponse("Hello World")
