from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the coffee subscription.")

def results(request, roaster_id):
