import reflex as rx

from wedding.styles import Color, Size
from wedding.styles.fonts import Font, FontHeight, FontWeight


def countdown_numbers(element: str) -> rx.Component:
    return rx.text(
        id=element,
        font_size=[
            "1.7em",
            Size.BIG.value,
            Size.BIG.value,
            Size.BIG.value,
            Size.BIG.value,
        ],
        color=Color.NUMBERS_COUNTDOWN.value,
        width="100%",
        font_family=Font.TITLE.value,
        text_align="center",
        font_style="normal",
        font_weight=FontWeight.MEDIUM_INSIDE_TEXTS.value,
        line_height=FontHeight.NORMAL.value,
    )
