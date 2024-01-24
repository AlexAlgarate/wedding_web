import reflex as rx

from wedding import utils
from wedding.components import card, icon_section, text_paragraph, title_section
from wedding.routes import IconRoutes as icon

from .components import destination, origin


def bus_service() -> rx.Component:
    return card(
        icon_section(icon=icon.ICON_BUS.value),
        title_section(title=utils.but_title),
        text_paragraph(utils.bus_text),
        origin(),
        destination(),
    )
