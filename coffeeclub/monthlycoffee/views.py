from django.shortcuts import render
from . import get_roasters_data
from . import set_roaster_data

def index(request):
    roaster = get_roasters_data.get_last_month_roaster()
    template = 'monthlycoffee/index.html'
    context = {"last_month_roaster": roaster}
    return render(request, template, context)

def results(request):
    roaster = get_roasters_data.get_next_roaster()
    template = 'monthlycoffee/results.html'
    context = { "roaster_of_the_month": roaster }
    return render(request, template, context)

def rate(request, roaster_id):
    roaster = get_roasters_data.get_roaster(roaster_id)
    template = 'monthlycoffee/rate.html'
    context = {"last_month_roaster": roaster}
    return render(request, template, context)