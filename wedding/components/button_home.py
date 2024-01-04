import reflex as rx

from wedding.styles.style import Size


def button_home(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            text,
            padding=Size.DEFAULT.value,
            border_radius=Size.MEDIUM_SMALL.value,
            width="100%",
        ),
        href=url,
        is_external=True,
    )
