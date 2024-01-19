import reflex as rx

from wedding.styles import Color, Size


def divider(section: bool = True, width: str = "65%") -> rx.Component:
    return rx.cond(
        section,
        rx.divider(
            orientation="horizontal",
            variant="solid",
            border_color=Color.TEXT_DEFAULT.value,
            width=width,
            padding_top="1.25em",
        ),
        rx.divider(
            orientation="horizontal",
            variant="solid",
            border_color=Color.TEXT_DEFAULT.value,
            width=width,
            padding_top=Size.SMALL.value,
        ),
    )
