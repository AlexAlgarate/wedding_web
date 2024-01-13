import reflex as rx

import wedding.urls as url
from wedding import utils as utils
from wedding.components import button, header_text
from wedding.routes import FileRoutes as file
from wedding.styles.style import Size

from .components import countdown_text

# from .components import button_date, countdown_text,


def countdown() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            header_text(utils.countdown_heading, style={"margin_top": "-0.15em"}),
        ),
        rx.hstack(countdown_text()),
        rx.hstack(button(button_name="Guardar fecha", url=url.CALENDAR_HTML)),
        # rx.hstack(button_date(url=url.CALENDAR_HTML)),
        rx.script(
            src=file.JS_COUNTDOWN.value,
        ),
        width="100%",
        margin=Size.BIG.value,
    )
