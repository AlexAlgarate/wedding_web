import reflex as rx

from wedding import utils
from wedding.components import icon_section, texts_lines
from wedding.routes import IconRoutes as icon
from wedding.styles import Size, style
from wedding.styles.fonts import FontWeight


def destination() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            icon_section(icon=icon.ICON_UBICATION.value, width=Size.BIG.value),
            rx.text(
                "VUELTA",
                font_weight=FontWeight.MEDIUM_INSIDE_TEXTS.value,
                font_size=Size.TEXT_SECTION.value,
            ),
            align_items="center",
        ),
        *texts_lines(
            utils.origin_address,
            (utils.wedding_place, style.bold_style_bus),
            utils.destination,
            (utils.origin_address, style.bold_style_bus),
            utils.destination_bus_schedule,
        ),
    )
