from typing import List

import reflex as rx

from wedding.styles import Font, Size


def wedding_date_header(list_date: List[str]) -> rx.Component:
    return rx.box(
        date_component(list_date[0]),
        rx.span(list_date[3], font_size="1.25em"),
        date_component(list_date[1]),
        rx.span(list_date[3], font_size="1.25em"),
        date_component(list_date[2]),
        font_family=Font.TITLE.value,
        font_size=[
            Size.LARGE.value,
            Size.LARGE.value,
            Size.BIG.value,
            Size.BIG.value,
            Size.BIG.value,
        ],
        width="100%",
    )


def date_component(date_element: str) -> rx.Component:
    return rx.span(date_element, font_size=Size.LARGE.value)
