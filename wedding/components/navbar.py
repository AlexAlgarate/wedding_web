import reflex as rx

import wedding.urls as url
import wedding.utils as utils
from wedding.components.link_navbar import link_navbar
from wedding.components.menu_bar import menu_bar
from wedding.routes import FileRoutes as file
from wedding.routes import Route
from wedding.styles.style import Size


def navbar() -> rx.Component:
    return rx.hstack(
        link_navbar(
            title=rx.image(
                src=file.IMAGE_HOME.value,
                alt=utils.alt_image_home,
            ),
            url=Route.INDEX.value,
            is_external=False,
        ),
        rx.spacer(),
        rx.text(utils.initials_navbar, text_align="center"),
        rx.spacer(),
        menu_bar(
            menu_items=utils.menu_items,
            urls_list=utils.url_list,
            is_external_list=utils.is_external,
            icon="menu_icon",
            alt=utils.alt_image_menu,
        ),
        position="sticky",
        padding_y=Size.DEFAULT.value,
        padding_x=Size.BIG.value,
        z_index="999",
        top="0",
        width="100%",
        class_name="navbar_wedding",
    )
