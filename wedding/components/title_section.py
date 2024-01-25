import reflex as rx

from wedding.styles import style


def title_section(title: str) -> rx.Component:
    return rx.heading(title, style=style.TITLE_STYLE)
