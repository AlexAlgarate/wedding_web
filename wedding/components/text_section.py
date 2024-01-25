import reflex as rx

from wedding.styles import style


def text_section(text: str) -> rx.Component:
    return rx.text(text, style=style.TEXT_SECTION_STYLE)
