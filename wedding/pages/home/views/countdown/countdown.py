import reflex as rx

import wedding.urls as url
from wedding import utils as utils
from wedding.components import secondary_button, text_section
from wedding.styles import Color

from .components import countdown_numbers, element_date


def countdown() -> rx.Component:
    return rx.flex(
        text_section(utils.countdown_text),
        rx.flex(
            rx.vstack(
                countdown_numbers("days"),
                element_date("Días"),
            ),
            rx.vstack(
                countdown_numbers("hours"),
                element_date("horas"),
            ),
            rx.vstack(
                countdown_numbers("minutes"),
                element_date("mins"),
            ),
            rx.vstack(
                countdown_numbers("seconds"),
                element_date("segs"),
            ),
            padding="16px 0px",
            justify="center",
            align="center",
            gap="16px",
            align_self="stretch",
            background=Color.COUNTDOWN_BACKGROUND.value,
        ),
        secondary_button(utils.countdown_button, url=url.CALENDAR_HTML),
        direction="column",
        align="center",
        justify="center",
        gap="16px",
    )
