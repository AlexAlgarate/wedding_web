import reflex as rx

from wedding.styles import Size


def countdown_text() -> rx.Component:
    return rx.text(
        id="countdown",
        margin_bottom=Size.SMALL.value,
        font_size=[
            "1.7em",
            Size.BIG.value,
            Size.BIG.value,
            Size.BIG.value,
            Size.BIG.value,
        ],
    )
