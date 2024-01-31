import reflex as rx

from wedding.styles import Color
from wedding.styles.fonts import Font, FontHeight, FontWeight


def element_date(element: str) -> rx.Component:
    return rx.text(
        element,
        color=Color.TEXT_COUNTDOWN.value,
        text_align="center",
        font_family=Font.DEFAULT.value,
        font_size="16px",
        font_style="normal",
        font_weight=FontWeight.MEDIUM_INSIDE_TEXTS.value,
        line_height=FontHeight.NORMAL.value,
    )
