import reflex as rx

from wedding import utils
from wedding.styles import style


def farewell_message() -> rx.Component:
    """
    Creates a centered heading component for a farewell
    message displayed at the bottom of the page.

    Returns:
        rx.Component: The farewell message component.
    """

    return rx.center(
        rx.heading(
            utils.bottom_text,
            size="2xl",
            style=style.BOTTOM_TEXT_STYLE,
        )
    )
