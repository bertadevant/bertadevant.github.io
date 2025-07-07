from .models import Rating
from . import get_roasters_data


def save_new_rating(roasting_id, score, review):
    roaster = get_roasters_data.get_roaster(roasting_id)
    rating = Rating.objects.create(roaster=roaster, rating=score, review=review)