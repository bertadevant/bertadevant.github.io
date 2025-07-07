from django.db import models
from .tag import Tag
from django.db.models import Avg

class CoffeeRoaster(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField()
    image = models.ImageField(upload_to="roasters_assets", null = True)
    tags = models.ManyToManyField(Tag)
    def __str__(self):
        return self.name

    def website_formatted(self):
        return f'<a href="{self.website}">{self.name}</a>'

    def rating(self):
        all_ratings = self.ratings.all()
        return self.ratings.aggregate(Avg('score'))

    """Weight is how much a roaster will be chosen by random, higher is better goes up to 5"""
    def weight(self):
        all_tags = self.tags.all()
        return all_tags.aggregate('value')