import reflex as rx

import wedding.urls as url
from wedding import utils as utils
from wedding.components.button_home import button_home
from wedding.routes import FileRoutes as file
from wedding.styles.fonts import Font
from wedding.styles.style import Size


def countdown() -> rx.Component:
    return rx.vstack(
        rx.heading(
            utils.countdown_heading,
            margin_top="-0.15em",
            # padding=Size.SMALL.value,
            align_items="center",
        ),
        rx.text(
            id="countdown",
            margin_left=Size.MEDIUM.value,
            font_family=Font.TITLE.value,
            font_size="100%",
            margin_bottom=Size.SMALL.value,
        ),
        button_home(url=url.CALENDAR_HTML),
        rx.script(src=file.JS_COUNTDOWN.value),
        width="100%",
        margin=Size.BIG.value,
        font_size=Size.BIG.value,
    )
