import reflex as rx

from wedding.styles import Size
from wedding.styles.colors import TextColor


def icon_section(icon: str) -> rx.Component:
    return rx.image(
        src=icon,
        color=TextColor.DEFAULT.value,
        width=Size.VERY_BIG.value,
        max_height="auto",
    )
