import reflex as rx

from wedding.styles import Color, Size


def countdown_text() -> rx.Component:
    return rx.text(
        id="countdown",
        font_size=[
            "1.7em",
            Size.BIG.value,
            Size.BIG.value,
            Size.BIG.value,
            Size.BIG.value,
        ],
        color=Color.TITLE.value,
    )
