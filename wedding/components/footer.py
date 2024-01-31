import reflex as rx

from wedding.styles import Color, Font, FontWeight


def footer() -> rx.Component:
    return rx.center(
        rx.heading(
            "Te esperamos",
            size="2xl",
            font_family=Font.TITLE.value,
            font_weight=FontWeight.MEDIUM.value,
            font_style="normal",
            line_height="normal",
            color=Color.TITLES.value,
            position="relative",
            top="50px",
        )
    )
