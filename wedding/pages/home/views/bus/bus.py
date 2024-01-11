import reflex as rx

from wedding.components.title_section import title_section
from wedding.routes import IconRoutes as icon
from wedding.components.icon_section import icon_section


def bus_service() -> rx.Component:
    return rx.vstack(
        title_section("Servicio de autobuses"),
        icon_section(icon=icon.ICON_BUS.value),
        rx.spacer(),
    )
