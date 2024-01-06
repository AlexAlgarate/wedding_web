import reflex as rx

from wedding.styles import colors
from wedding.styles import style as style
from wedding.styles.style import Size


def button_home(url: str) -> rx.Component:
    return rx.button(
        rx.html(url),
        padding=Size.DEFAULT.value,
        background=colors.Color.BUTTON_SAVE_DATE.value,
        border_radius=Size.MEDIUM_SMALL.value,
        width="50%",
        text_align="center",
        style=style.shadow_style,
    )
