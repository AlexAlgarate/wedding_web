import reflex as rx

from wedding.components import divider, icon_section, title_section
from wedding.routes import IconRoutes as icon

from .components import destination, origin
from wedding.styles import Size


def bus_service() -> rx.Component:
    return rx.box(
        rx.vstack(
            title_section(title="Servicio de autobuses"),
            icon_section(icon=icon.ICON_BUS.value),
            divider(width="50%"),
            rx.spacer(),
            origin(),
            rx.spacer(),
            rx.spacer(),
            rx.spacer(),
            rx.spacer(),
            destination(),
            margin_bottom=Size.BIG.value,
        ),
    )
