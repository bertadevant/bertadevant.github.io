from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("templates/results", views.results, name="results"),
    # the 'name' value as called by the {% url %} template tag
    path("templates/rate/<int:roaster_id>/", views.rate, name="rate")
]