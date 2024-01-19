import reflex as rx

from wedding import icon, utils
from wedding.components import (
    card,
    divider,
    icon_section,
    text_paragraph,
    title_section,
)

from .components import destination, origin


def bus_service() -> rx.Component:
    return card(
        icon_section(icon=icon.ICON_BUS.value),
        title_section(title=utils.but_title),
        divider(width="50%", section=False),
        text_paragraph(utils.bus_text),
        origin(),
        destination(),
    )


# def bus_service() -> rx.Component:
#     return rx.box(
#         rx.vstack(
#             icon_section(icon=icon.ICON_BUS.value),
#             title_section(title=utils.but_title),
#             divider(width="50%", section=False),
#             text_paragraph(utils.bus_text),
#             *spacer(spacers=1),
#             origin(),
#             *spacer(spacers=2),
#             destination(),
#             margin_bottom=Size.BIG.value,
#         ),
#     )
