import reflex as rx

from wedding.styles import Color, Size


def divider(section: bool = True, width: str = "65%") -> rx.Component:
    """
    Create a horizontal divider component.

    Parameters:
    - section (bool): If True, includes additional padding for section dividers.
    - width (str): The width of the divider.

    Returns:
    - rx.Component: A Reflex component representing the horizontal divider.
    """

    return rx.cond(
        section,
        rx.divider(
            orientation="horizontal",
            variant="solid",
            border_color=Color.DEFAULT_TEXT.value,
            width=width,
            padding_top="1.25em",
        ),
        rx.divider(
            orientation="horizontal",
            variant="solid",
            border_color=Color.DEFAULT_TEXT.value,
            width=width,
            padding_top=Size.SMALL.value,
        ),
    )
