from typing import List

import reflex as rx

from wedding.components.link_navbar import link_navbar
from wedding.styles.style import Size


def menu_bar(
    menu_items: List[str],
    icon: str,
    urls_list: List[str],
    is_external_list: List[bool],
    alt: str,
) -> rx.Component:
    menu_content = []

    for item_name, url, is_external in zip(menu_items, urls_list, is_external_list):
        menu_content.append(link_navbar(item_name, url, is_external))

        if item_name != menu_items[-1]:
            menu_content.append(rx.menu_divider())
    return rx.menu(
        rx.menu_button(rx.image(src=f"/{icon}.png", alt=alt)),
        rx.menu_list(
            *menu_content,
            padding=Size.DEFAULT.value,
        ),
        close_on_blur=True,
        close_on_select=True,
        width="100%",
    )
