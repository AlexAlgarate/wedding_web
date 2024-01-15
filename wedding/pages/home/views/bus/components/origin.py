import reflex as rx

from wedding import utils
from wedding.components import icon_section
from wedding.routes import IconRoutes as icon
from wedding.styles import Size, style
from wedding.styles.fonts import FontWeight

from .bus_texts import bus_texts


def origin() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            icon_section(icon=icon.ICON_UBICATION.value, width=Size.BIG.value),
            rx.text(
                "IDA",
                font_weight=FontWeight.MEDIUM_INSIDE_TEXTS.value,
                font_size="1.25em",
            ),
            align_items="center",
        ),
        *bus_texts(
            utils.origin,
            (utils.origin_address, style.bold_style_bus),
            utils.destination,
            (utils.wedding_place, style.bold_style_bus),
            utils.origin_bus_schedule,
        ),
    )
