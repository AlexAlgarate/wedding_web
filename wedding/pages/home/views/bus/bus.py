import reflex as rx

from wedding.components import divider, icon_section, spacer, title_section
from wedding.routes import IconRoutes as icon
from wedding.styles import Size

from .components import destination, origin


def bus_service() -> rx.Component:
    return rx.box(
        rx.vstack(
            title_section(title="Servicio de autobuses"),
            icon_section(icon=icon.ICON_BUS.value),
            divider(width="50%"),
            rx.spacer(),
            origin(),
            *spacer(spacers=4),
            destination(),
            margin_bottom=Size.BIG.value,
        ),
    )
