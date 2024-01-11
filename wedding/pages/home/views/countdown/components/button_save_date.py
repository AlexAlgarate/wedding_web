import reflex as rx

from wedding.styles import Size
from wedding.styles.colors import Color
from wedding.styles import style as style


def button_date(url: str) -> rx.Component:
    return rx.button(
        rx.html(
            url,
            width="100%",
            font_size=[
                Size.DEFAULT.value,
                Size.DEFAULT.value,
                Size.DEFAULT.value,
                Size.LARGE.value,
                Size.LARGE.value,
            ],
        ),
        padding=Size.DEFAULT.value,
        background=Color.BUTTON_SAVE_DATE.value,
        border_radius=Size.MEDIUM_SMALL.value,
        width="100%",
        text_align="center",
        margin_bottom=Size.DEFAULT.value,
        box_shadow="""
        inset 0 -3em 3em rgba(0, 0, 0, 0.1),
        0.3em 0.3em 1em rgba(0, 0, 0, 0.3)
        """,
    )
