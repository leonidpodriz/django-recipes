from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from typing import Union
from django.shortcuts import render, get_object_or_404
from .models import Recipe


def recipes_list(request: HttpRequest) -> HttpResponse:
    recipes = Recipe.objects.all()

    return render(request, "recipes.html", context={"recipes": recipes})


def recipe_details(request: HttpRequest, recipe_id: int) -> HttpResponse:
    # recipe = Recipe.objects.get(id=recipe_id)
    recipe = get_object_or_404(Recipe, id=recipe_id)

    return render(request, "recipe-details.html", context={"recipe": recipe})
