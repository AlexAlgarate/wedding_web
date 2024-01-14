import reflex as rx

from wedding.components import icon_section, title_section
from wedding.routes import IconRoutes as icon


def bus_service() -> rx.Component:
    return rx.vstack(
        title_section("Servicio de autobuses"),
        icon_section(icon=icon.ICON_BUS.value),
        rx.spacer(),
        rx.center(
            rx.text(
                "Quedan pocos días para la boda, apresúrense a comprar sus trajes y su Benzo",
                text_align="center",
            ),
        ),
    )
