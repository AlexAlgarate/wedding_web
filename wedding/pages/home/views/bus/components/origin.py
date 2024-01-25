import reflex as rx

from wedding import utils
from wedding.components import icon_section, texts_lines
from wedding.routes import IconRoutes as icon
from wedding.styles import FontWeight, Size, style


def origin() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            icon_section(icon=icon.ICON_UBICATION.value, width=Size.BIG.value),
        ),
        *texts_lines((utils.bus_origin_title, style.BUS_TITLE_SECTION)),
        rx.spacer(),
        _bus_text_origin(),
        width="100%",
    )


def _bus_text_origin() -> rx.Component:
    return rx.flex(
        rx.box(
            "Salida ",
            rx.span(utils.origin_bus_schedule, font_weight=FontWeight.BOLD.value),
            " desde ",
        ),
        rx.box(
            rx.span(utils.hotel_name, font_weight=FontWeight.BOLD.value),
        ),
        rx.box(
            rx.span(utils.hotel_address, font_weight=FontWeight.BOLD.value),
        ),
        direction="column",
        align="center",
        font_size=[
            Size.MAIN_TEXTS.value,
            Size.MAIN_TEXTS.value,
            Size.MAIN_TEXTS.value,
            Size.MAIN_TEXTS.value,
            Size.MAIN_TEXTS.value,
        ],
        max_width=style.MAX_WIDTH,
    )
