import reflex as rx

from wedding.styles import style
from wedding.styles.style import Size


def text_paragraph(text: str) -> rx.Component:
    return rx.text(
        text,
        max_width=style.MAX_WIDTH,
        padding=Size.ZERO.value,
        text_align="center",
        font_size=[
            Size.TEXT_SECTION.value,
            Size.LARGE.value,
            Size.LARGE.value,
            Size.LARGE.value,
            Size.LARGE.value,
        ],
        text_wrap="pretty",
        font_style="normal",
        line_height="normal",
        width="100%",
    )
