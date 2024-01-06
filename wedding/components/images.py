import reflex as rx

from wedding.styles import style
from wedding.styles.style import Size


def image_header(image: str, alt: str) -> rx.Component:
    return rx.image(
        src=image,
        margin_bottom=Size.MEDIUM.value,
        border_radius="12px 50px",
        style=style.shadow_style,
        alt=alt,
    )
