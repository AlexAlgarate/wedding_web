import reflex as rx

from wedding.styles import Size
from wedding.styles.fonts import Font


def countdown_text() -> rx.Component:
    return rx.text(
        id="countdown",
        margin_left=Size.MEDIUM.value,
        font_family=Font.TITLE.value,
        margin_bottom=Size.SMALL.value,
        font_size=[
            "1.8em",
            Size.BIG.value,
            Size.BIG.value,
            Size.BIG.value,
            Size.BIG.value,
        ],
    )
