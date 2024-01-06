import reflex as rx

from wedding import utils as utils
from wedding.styles import style
from wedding.styles.style import Size


def main_text() -> rx.Component:
    return rx.text(
        utils.main_text, max_width=style.MAX_WIDTH, padding=Size.MEDIUM.value
    )
