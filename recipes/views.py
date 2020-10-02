from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from .services import get_recipes_list, Recipe, get_recipe_details_or_none
from typing import Union


ADDITIONAL_STYLES = """<style>
div {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px 10px;
  border-bottom: 1px solid black;
  font-family: 'Roboto', sans-serif;
}
</style>"""


def recipes_list(request: HttpRequest) -> HttpResponse:
    recipes: list = get_recipes_list()
    html: str = ""

    for recipe_data in recipes:
        html += str(Recipe(**recipe_data))

    return HttpResponse(html + ADDITIONAL_STYLES)


def recipe_details(request: HttpRequest, recipe_id: int) -> HttpResponse:
    recipe: Union[Recipe, None] = get_recipe_details_or_none(recipe_id)

    if recipe is None:
        return HttpResponseNotFound("Recipe not found!")

    html = str(recipe)

    return HttpResponse(html + ADDITIONAL_STYLES)
