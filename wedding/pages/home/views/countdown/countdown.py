import reflex as rx

import wedding.urls as url
from wedding import utils as utils
from wedding.components import button, card, title_section
from wedding.routes import FileRoutes as file

from .components import countdown_text


def countdown() -> rx.Component:
    return card(
        rx.vstack(
            title_section(utils.countdown_title),
            rx.hstack(countdown_text()),
            rx.hstack(button(button_name="Guardar fecha", url=url.CALENDAR_HTML)),
            rx.script(
                src=file.JS_COUNTDOWN.value,
            ),
        ),
        style={"width": "100%"},
    )
