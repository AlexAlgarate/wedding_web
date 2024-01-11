import reflex as rx

import wedding.utils as utils
from wedding.components.link_navbar import link_navbar
from wedding.components.menu_bar import menu_bar
from wedding.routes import IconRoutes as icon
from wedding.routes import Route
from wedding.styles import style
from wedding.styles.fonts import FontHeight
from wedding.styles.style import Size


def navbar() -> rx.Component:
    return rx.hstack(
        link_navbar(
            title=rx.image(
                src=icon.ICON_IMAGE_HOME.value,
                alt=utils.alt_image_home,
            ),
            url=Route.INDEX.value,
            is_external=False,
        ),
        rx.spacer(),
        rx.text(
            utils.initials_navbar,
            text_align="center",
            font_size=[
                FontHeight.MEDIUM.value,
                FontHeight.BIG.value,
                FontHeight.BIG.value,
                FontHeight.BIG.value,
                FontHeight.BIG.value,
            ],
        ),
        rx.spacer(),
        menu_bar(
            menu_items=utils.menu_items,
            urls_list=utils.url_list,
            is_external_list=utils.is_external,
            icon=icon.ICON_MENU.value,
            alt=utils.alt_image_menu,
        ),
        position="sticky",
        padding_y=Size.DEFAULT.value,
        padding_x=Size.BIG.value,
        z_index="999",
        top="0",
        width="100%",
        style=style.NAVBAR_STYLE,
        class_name="navbar_wedding",
    )
