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
        linked_name: str = get_html_link(recipe_link, self.name)
        html_title: str = get_html_header(linked_name)
        html_description: str = get_html_paragraph(self.description)
        return get_html_container(html_title + html_description)

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


def get_html_header(text: str, level: int = 2) -> str:
    return f"<h{level}>{text}</h{level}>"


def get_html_paragraph(text: str) -> str:
    return f"<p>{text}</p>"


def get_html_container(text: str) -> str:
    return f"<div>{text}</div>"


def get_html_link(href: str, text: str) -> str:
    return f'<a href="{href}">{text}</a>'
