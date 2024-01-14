import reflex as rx

from wedding.styles import style
from wedding.styles.style import Size


def text_section(text: str) -> rx.Component:
    return rx.text(
        text,
        max_width=style.MAX_WIDTH,
        padding=Size.MEDIUM_SMALL.value,
        text_align="center",
        font_size=[
            Size.TEXT_SECTION.value,
            Size.LARGE.value,
            Size.LARGE.value,
            Size.LARGE.value,
            Size.LARGE.value,
        ],
        width="100%",
    )
