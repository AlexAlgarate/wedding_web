import reflex as rx

from wedding.styles import style


def element_date(text_date: str) -> rx.Component:
    return rx.text(text_date, style=style.COUNTDOWN_TEXT_STYLE)
