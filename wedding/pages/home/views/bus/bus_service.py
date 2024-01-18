import reflex as rx

from wedding import utils
from wedding.components import (
    divider,
    icon_section,
    spacer,
    text_paragraph,
    title_section,
)
from wedding.routes import IconRoutes as icon
from wedding.styles import Size

from .components import destination, origin


def bus_service() -> rx.Component:
    return rx.box(
        rx.vstack(
            icon_section(icon=icon.ICON_BUS.value),
            title_section(title=utils.but_title),
            divider(width="50%"),
            text_paragraph(utils.bus_text),
            *spacer(spacers=1),
            origin(),
            *spacer(spacers=2),
            destination(),
            margin_bottom=Size.BIG.value,
        ),
    )
