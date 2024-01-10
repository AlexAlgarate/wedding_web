import reflex as rx

from wedding.styles import style
from wedding.styles.style import Size


def main_text(text: str) -> rx.Component:
    return rx.text(text, max_width=style.MAX_WIDTH, padding=Size.MEDIUM.value)
