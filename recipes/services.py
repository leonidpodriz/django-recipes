from .db import FAKE_DATABASE


def get_recipes_list() -> list:
    return FAKE_DATABASE.get("recipes")


def get_html_header(text: str, level: int = 2) -> str:
    return f"<h{level}>{text}</h{level}>"


def get_html_paragraph(text: str) -> str:
    return f"<p>{text}</p>"


def get_html_container(text: str) -> str:
    return f"<div>{text}</div>"


class Recipe:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def __str__(self) -> str:
        html_title = get_html_header(self.name)
        html_description = get_html_paragraph(self.description)
        return get_html_container(html_title + html_description)
