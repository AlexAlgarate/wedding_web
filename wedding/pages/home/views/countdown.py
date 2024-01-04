import reflex as rx

from wedding import urls as url
from wedding import utils as utils
from wedding.components.button_home import button_home
from wedding.routes import FileRoutes as file
from wedding.styles.fonts import Font
from wedding.styles.style import Size


def countdown() -> rx.Component:
    return rx.vstack(
        rx.heading(
            utils.countdown_heading,
            margin=Size.ZERO.value,
            padding=Size.SMALL.value,
            align_items="center",
        ),
        rx.text(
            id="countdown",
            margin_left=Size.MEDIUM.value,
            font_family=Font.TITLE.value,
            font_size="100%",
        ),
        button_home(text=utils.save_date_button, url=url.CALENDAR_URL),
        rx.script(src=file.JS_COUNTDOWN.value),
        width="100%",
        margin=Size.BIG.value,
        font_size=Size.BIG.value,
    )
