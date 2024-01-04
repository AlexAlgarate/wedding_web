from typing import List

import reflex as rx

import wedding.utils as utils
from wedding.styles.fonts import Font, FontWeight
from wedding.styles.style import Size


def header(list_date: List[str]) -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading(
                utils.title_header,
                font_size=Size.MEDIUM_BIGGER.value,
                font_weight=FontWeight.MEDIUM.value,
            ),
            _wedding_date_header(list_date=list_date),
            font_family=Font.TITLE.value,
            align_items="center",
            width="100%",
        ),
    )


def _wedding_date_header(list_date: List[str]) -> rx.Component:
    return rx.box(
        date_component(list_date[0]),
        rx.span(list_date[3], font_size=Size.LARGE.value),
        date_component(list_date[1]),
        rx.span(list_date[3], font_size=Size.LARGE.value),
        date_component(list_date[2]),
        width="100%",
    )


def date_component(date_element: str) -> rx.Component:
    return rx.span(date_element, font_size=Size.BIG.value)
