import reflex as rx

from wedding import icon, utils
from wedding.components import icon_section, texts_lines
from wedding.styles import FontWeight, Size, style


def origin() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            icon_section(icon=icon.ICON_UBICATION.value, width=Size.BIG.value),
        ),
        *texts_lines((utils.bus_origin_title, style.style_title_bus)),
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
            rx.span(utils.origin_address, font_weight=FontWeight.BOLD.value),
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