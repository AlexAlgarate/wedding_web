import reflex as rx

import wedding.urls as url
from wedding import utils as utils
from wedding.components import secondary_button, text_section
from wedding.routes import FileRoutes
from wedding.styles import Color

from .components import countdown_numbers, element_date


def countdown() -> rx.Component:
    return rx.flex(
        text_section(utils.countdown_text),
        rx.flex(
            rx.vstack(
                countdown_numbers(element="days"),
                element_date(text_date="Días"),
            ),
            rx.vstack(
                countdown_numbers(element="hours"),
                element_date(text_date="horas"),
            ),
            rx.vstack(
                countdown_numbers(element="minutes"),
                element_date(text_date="mins"),
            ),
            rx.vstack(
                countdown_numbers(element="seconds"),
                element_date(text_date="segs"),
            ),
            rx.script(src=FileRoutes.JS_COUNTDOWN.value),
            padding="16px 0px",
            justify="center",
            align="center",
            gap="1.5em",
            align_self="stretch",
            background=Color.COUNTDOWN_BACKGROUND.value,
        ),
        secondary_button(utils.countdown_button, url=url.CALENDAR_HTML),
        direction="column",
        align="center",
        justify="center",
        gap="16px",
    )
