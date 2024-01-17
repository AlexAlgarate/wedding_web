from typing import List

import reflex as rx

from wedding import icon, utils
from wedding.styles.colors import Color
from wedding.styles.style import Size

from .link_navbar import link_navbar


def menu_bar(
    menu_items: List[str],
    urls_list: List[str],
    is_external_list: List[bool],
) -> rx.Component:
    menu_content = []

    for item_name, url, is_external in zip(menu_items, urls_list, is_external_list):
        menu_content.append(link_navbar(item_name, url, is_external))

        if item_name != menu_items[-1]:
            menu_content.append(
                rx.menu_divider(variant="solid", border_color=Color.TEXT_DEFAULT.value)
            )
    return rx.menu(
        rx.menu_button(rx.image(src=icon.ICON_MENU.value, alt=utils.alt_image_menu)),
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
            border="solid",
            border_width="0 1px 1px 0",
            border_color=Color.TEXT_DEFAULT.value,
            box_shadow=f"3px 2.5px 8px 1px {Color.DEFAULT_OPACITY.value}",
            width="100%",
        ),
        close_on_blur=True,
        is_lazy=True,
        close_on_select=True,
        width="100%",
    )
