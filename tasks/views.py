from django.http import HttpResponse

def home(request):
    return HttpResponse("Hola, esta es mi primera aplicación django")