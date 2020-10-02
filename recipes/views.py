from django.http import HttpRequest, HttpResponse
from .services import get_recipes_list, Recipe


def recipes_list(request: HttpRequest):
    recipes: list = get_recipes_list()
    html: str = ""

    for recipe_data in recipes:
        html += str(Recipe(**recipe_data))

    return HttpResponse(html)
