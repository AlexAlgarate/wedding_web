import reflex as rx

from wedding import utils
from wedding.styles import Color, Size

from .link_navbar import link_navbar


def menu_bar(icon: rx.Component) -> rx.Component:
    """
    Creates a responsive menu bar component with links and a hamburger menu icon.

    Returns:
        rx.Component: The menu bar component.
    """

    menu_content = []

    for item_name, url in zip(utils.menu_items, utils.href_list):
        menu_content.append(link_navbar(item_name, url))

        if item_name != utils.menu_items[-1]:
            menu_content.append(rx.menu_divider())

    return rx.menu(
        rx.menu_button(icon),
        rx.menu_list(
            *menu_content,
            padding=Size.DEFAULT.value,
            background_color=Color.BACKGROUND.value,
            font_size=[
                "1.15em",
                Size.LARGE.value,
                Size.LARGE.value,
                Size.LARGE.value,
                Size.LARGE.value,
            ],
            box_shadow=f"1px 1px 4px 1px {Color.PURPLE_OPACITY.value}",
            width="100%",
        ),
        close_on_blur=True,
        close_on_select=True,
        is_lazy=True,
        width="100%",
    )
