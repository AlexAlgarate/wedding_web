import reflex as rx

from wedding.styles.fonts import FontWeight
from wedding.styles.style import Size


def link_navbar(title: str, url: str, is_external=True) -> rx.Component:
    return rx.link(
        rx.text(
            title,
            font_weight=FontWeight.LIGHT.value,
            font_size=Size.DEFAULT.value,
        ),
        href=url,
        is_external=True if is_external else False,
        text_align="start",
    )
