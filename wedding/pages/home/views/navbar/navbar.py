import reflex as rx

from wedding.styles import Color, style

from .components import initials_navbar, menu_bar, menu_icon


def navbar() -> rx.Component:
    """
    Creates a responsive navbar component with a menu bar, initials, and a notification bell.

    Returns:
        rx.Component: The navbar component.
    """

    return rx.box(
        rx.hstack(
            menu_bar(
                icon=menu_icon(
                    tag="hamburger",
                    color=Color.TITLES.value,
                )
            ),
            rx.spacer(),
            initials_navbar(),
            rx.spacer(),
            menu_icon(tag="bell"),
        ),
        style=style.NAVBAR_STYLE,
        class_name="navbar_wedding",
    )
