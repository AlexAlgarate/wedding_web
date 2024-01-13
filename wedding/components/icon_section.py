import reflex as rx

from wedding.styles import Size
from wedding.styles.colors import Color


def icon_section(icon: str) -> rx.Component:
    return rx.image(
        src=icon,
        color=Color.TEXT_DEFAULT.value,
        width=Size.VERY_BIG.value,
        max_height="auto",
    )
