import reflex as rx

from wedding.styles import style


def button(button_name: str, url: str, **args) -> rx.Component:
    return rx.link(
        rx.button(button_name, style=style.MAIN_BUTTON_STYLE),
        href=url,
        is_external=True,
    )
