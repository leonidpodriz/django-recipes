from .db import FAKE_DATABASE
from typing import Union
from django.urls import reverse, reverse_lazy


class Recipe:
    recipes_list = reverse_lazy("recipes-list")

    def __init__(self, name: str, description: str, id: int):
        self.name = name
        self.description = description
        self.id = id

    def __str__(self) -> str:
        recipe_link: str = self.get_recipe_link()
        linked_name: str = HTMLElement(self.name).link(recipe_link)
        html_title: str = HTMLElement(linked_name).header()
        html_description: str = HTMLElement(self.description).paragraph()
        return HTMLElement(html_title + html_description).container()

    def get_recipe_link(self) -> str:
        return reverse("recipe-details", kwargs={"recipe_id": self.id})


def get_recipes_list() -> list:
    return FAKE_DATABASE.get("recipes")


def get_recipe_details_or_none(recipe_id: int) -> Union[None, Recipe]:
    recipes: list = get_recipes_list()

    for recipe_data in recipes:
        if recipe_data.get("id") == recipe_id:
            return Recipe(**recipe_data)

    return None


class HTMLElement:
    def __init__(self, text: str):
        self.text = text

    def link(self, href: str) -> str:
        return f'<a href="{href}">{self.text}</a>'

    def container(self) -> str:
        return f"<div>{self.text}</div>"

    def paragraph(self) -> str:
        return f"<p>{self.text}</p>"

    def header(self, level: int = 2) -> str:
        return f"<h{level}>{self.text}</h{level}>"
