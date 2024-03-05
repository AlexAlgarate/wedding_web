import reflex as rx

from wedding import utils
from wedding.components.navbar.components import link_navbar
from wedding.styles import Color, Size

from .components import initials_navbar, menu_icon


def menu_buger() -> rx.Component:
    menu_items = [
        rx.menu.item(
            link_navbar(title=title, url=url),
            color_scheme="purple",
        )
        for title, url in utils.menu_data.items()
    ]

    return rx.link(
        rx.menu.root(
            rx.menu.trigger(menu_icon(tag="menu", color=Color.TITLES.value)),
            rx.menu.content(
                *menu_items,
                size="2",
            ),
        )
    )


def navbar() -> rx.Component:
    """
    Creates a responsive navbar component with a menu bar, initials, and a notification bell.

    Returns:
        rx.Component: The navbar component.
    """

    return rx.hstack(
        menu_buger(),
        rx.spacer(),
        initials_navbar(),
        rx.spacer(),
        menu_icon(tag="bell"),
        class_name="navbar_wedding",
        id="navbar",
        box_shadow=f"0px 1px 5px 1px {Color.PURPLE_OPACITY.value}",
        position="sticky",
        padding_top=Size.MEDIUM_SMALL.value,
        padding_bottom=Size.ZERO.value,
        z_index="5",
        justify_content="center",
        top="0",
        background_color=Color.CONTENT.value,
        width="100%",
        align="center",
        justify="center",
    )
