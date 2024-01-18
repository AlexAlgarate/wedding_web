import reflex as rx

from wedding import utils
from wedding.components import icon_section, texts_lines
from wedding.routes import IconRoutes as icon
from wedding.styles import Size, style
from wedding.styles.fonts import FontWeight


def destination() -> rx.Component:
    return rx.vstack(
        rx.hstack(icon_section(icon=icon.ICON_UBICATION.value, width=Size.BIG.value)),
        *texts_lines((utils.bus_destination_title, style.style_title_bus)),
        rx.spacer(),
        _bus_text_destination(),
        width="100",
    )


def _bus_text_destination() -> rx.Component:
    return rx.flex(
        rx.box("Salidas de La Agripina "),
        rx.box(
            "a las ",
            rx.span("02:00", font_weight=FontWeight.BOLD.value),
            "y a las ",
            rx.span("05:00", font_weight=FontWeight.BOLD.value),
        ),
        rx.box("con destino"),
        rx.box(rx.span(utils.origin_address, font_weight=FontWeight.BOLD.value)),
        direction="column",
        align="center",
        text_wrap="pretty",
        font_size=[
            Size.MAIN_TEXTS.value,
            Size.MAIN_TEXTS.value,
            Size.MAIN_TEXTS.value,
            Size.MAIN_TEXTS.value,
            Size.MAIN_TEXTS.value,
        ],
    )
