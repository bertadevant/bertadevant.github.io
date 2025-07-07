from django.http import HttpResponse
from django.template import loader

from .models import CoffeeRoaster

def index(request):
    return HttpResponse("Hello, world. You're at the coffee subscription.")

def results(request, roaster_id):
    roaster = models.Roaster.objects.get(id=roaster_id)
    template = 'monthlycoffee/results.html'
    context = { "roaster_of_the_month": roaster }
    return HttpResponse(template.render(context, request))