from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100)
    value = models.FloatField()

    def __str__(self):
        return self.name

class CoffeeRoaster(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField()
    rating = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag)
    def __str__(self):
        return self.name

