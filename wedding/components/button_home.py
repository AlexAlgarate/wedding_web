import reflex as rx

from wedding.styles import Size, colors
from wedding.styles import style as style


def button_home(url: str) -> rx.Component:
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
        background=colors.Color.BUTTON_SAVE_DATE.value,
        border_radius=Size.MEDIUM_SMALL.value,
        width="100%",
        text_align="center",
        margin_bottom=Size.DEFAULT.value,
        style=style.shadow_style,
    )
