import reflex as rx

import wedding.utils as utils
from wedding.styles import Size
from wedding.styles.colors import Color
from wedding.styles.fonts import Font, FontWeight

from .components import initials_navbar


def navbar() -> rx.Component:
    return rx.center(
        rx.hstack(
            initials_navbar(initials=utils.initials_navbar),
        ),
        # menu_bar(
        #     menu_items=utils.menu_items,
        #     urls_list=utils.url_list,
        #     is_external_list=utils.is_external,
        # ),
        # rx.spacer(),
        # style=style.NAVBAR_STYLE,
        box_shadow=f"0px 1px 5px 1px {Color.DEFAULT_OPACITY.value}",
        width="100%",
        position="sticky",
        padding_top="0.75em",
        padding_bottom=Size.ZERO.value,
        # padding_x=Size.BIG.value,
        z_index="999",
        top="0",
        background_color=Color.CONTENT.value,
        color=Color.TEXT_DEFAULT.value,
        font_family=Font.TITLE.value,
        font_weight=FontWeight.MEDIUM.value,
        # font_size=Size.DEFAULT.value,
        class_name="navbar_wedding",
    )


# def navbar() -> rx.Component:
#     return rx.hstack(
#         link_navbar(
#             title=rx.image(
#                 src=icon.ICON_IMAGE_HOME.value,
#                 alt=utils.alt_image_home,
#             ),
#             url=Route.INDEX.value,
#             is_external=False,
#         ),
#         rx.spacer(),
#         rx.text(
#             utils.initials_navbar,
#             text_align="center",
#             font_size=[
#                 FontHeight.MEDIUM.value,
#                 FontHeight.BIG.value,
#                 FontHeight.BIG.value,
#                 FontHeight.BIG.value,
#                 FontHeight.BIG.value,
#             ],
#         ),
#         rx.spacer(),
#         m        # menu_bar(
#     menu_items=utils.menu_items,
#     urls_list=utils.url_list,
#     is_external_list=utils.is_external,
# ),

#         position="sticky",
#         padding_y=Size.DEFAULT.value,
#         padding_x=Size.BIG.value,
#         z_index="999",
#         top="0",
#         width="100%",
#         style=style.NAVBAR_STYLE,
#         class_name="navbar_wedding",
#     )
