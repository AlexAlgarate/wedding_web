import reflex as rx

from wedding import utils
from wedding.components import icon_section
from wedding.routes import IconRoutes as icon
from wedding.styles import Size

from .bus_texts import bus_texts


def destination() -> rx.Component:
    return rx.vstack(
        icon_section(icon=icon.ICON_UBICATION.value, width=Size.BIG.value),
        *bus_texts(
            utils.origin,
            utils.wedding_place,
            utils.destination,
            utils.origin_address,
            utils.destination_bus_schedule,
        ),
    )
