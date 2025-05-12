import reflex as rx

import wedding.urls as url
from wedding import utils as utils
from wedding.components import secondary_button, text_section
from wedding.styles import Color, Font, FontHeight, FontWeight, Size


def finished_wedding(text: str) -> rx.Component:
    return rx.text(
        text,
        color=Color.NUMBERS_COUNTDOWN.value,
        width="100%",
        height="100%",
        font_family=Font.TITLE.value,
        text_align="center",
        font_style="normal",
        font_weight=FontWeight.MEDIUM_INSIDE_TEXTS.value,
        line_height=FontHeight.NORMAL.value,
        font_size=[
            Size.BIG.value,
            Size.BIG.value,
            Size.BIG.value,
            Size.BIG.value,
            Size.BIG.value,
        ],
    )


def countdown() -> rx.Component:
    """
    Creates a countdown component for the wedding date.

    Returns:
        rx.Component: The countdown component.
    """

    # As the wedding has already celebrated, this lines breake the UI.
    # countdown_elements = [
    #     create_countdown_vstack(element="days", text_date="Days"),
    #     create_countdown_vstack(element="hours", text_date=""),
    #     create_countdown_vstack(element="minutes", text_date=""),
    #     create_countdown_vstack(element="seconds", text_date=""),
    # ]
    return rx.vstack(
        text_section(utils.countdown_text),
        secondary_button(utils.countdown_button, url=url.CALENDAR_HTML),
        rx.flex(
            # As the wedding has already celebrated, this lines breake the UI.
            # *countdown_elements,
            # rx.script(src=FileRoutes.JS_COUNTDOWN.value),
            finished_wedding("¡Ya hemos celebrado nuestra boda!"),
            justify="center",
            align="center",
            padding="16px 0px",
            gap="1.5em",
            align_self="stretch",
            background=Color.COUNTDOWN_BACKGROUND.value,
            width="100%",
        ),
        align="center",
        gap="16px",
        id="wedding_date",
        width="100%",
    )
