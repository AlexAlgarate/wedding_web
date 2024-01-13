import reflex as rx

from wedding.components import icon_section, title_section
from wedding.routes import IconRoutes as icon


def bus_service() -> rx.Component:
    return rx.vstack(
        title_section("Servicio de autobuses"),
        icon_section(icon=icon.ICON_BUS.value),
        rx.spacer(),
    )
