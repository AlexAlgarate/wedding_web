import reflex as rx

from wedding.styles import Size, style


def countdown_numbers(element: str) -> rx.Component:
    return rx.text(
        id=element,
        style=style.COUNTDOWN_NUMBERS_STYLE,
    )
