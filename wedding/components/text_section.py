import reflex as rx

from wedding.styles import Size, style


def text_paragraph(text: str) -> rx.Component:
    return rx.text(
        text,
        max_width=style.MAX_WIDTH,
        padding=Size.SMALL.value,
        text_align="center",
        font_size=[
            Size.MAIN_TEXTS.value,
            Size.MAIN_TEXTS.value,
            Size.MAIN_TEXTS.value,
            Size.MAIN_TEXTS.value,
            Size.MAIN_TEXTS.value,
        ],
        text_wrap="pretty",
        font_style="normal",
        line_height="normal",
        width="100%",
    )
