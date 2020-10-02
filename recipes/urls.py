from django.urls import path
from .views import recipes_list, recipe_details

urlpatterns = [
    path("", recipes_list, name="recipes-list"),
    path("<int:recipe_id>/", recipe_details, name="recipe-details"),
]
