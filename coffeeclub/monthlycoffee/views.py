from django.shortcuts import render
from django.templatetags.static import static
from . import get_roasters_data
from . import set_roaster_data
import random

def index(request):
    roaster = get_roasters_data.get_last_month_roaster()
    banner_num = random.randint(1, 30)
    banner_url = static(f"monthlycoffee/images/banner_images/{banner_num}.jpg")
    template = 'monthlycoffee/index.html'
    context = {
        "last_month_roaster": roaster,
        "banner_url": banner_url
    }
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