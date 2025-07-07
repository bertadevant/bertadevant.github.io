from .models import CoffeeRoaster
from django.shortcuts import get_object_or_404, get_list_or_404
import random

def get_last_month_roaster():
    roaster_query = CoffeeRoaster.objects.filter(tags__name='Last Time').first()
    return get_object_or_404(roaster_query)

def get_roaster(id):
    return get_object_or_404(CoffeeRoaster, pk=id)

def get_next_roaster():
    roasters = CoffeeRoaster.objects.all()
    weights = [roaster.weight for roaster in roasters]
    return random.choices(roasters, weights=weights, k=1)[0]
