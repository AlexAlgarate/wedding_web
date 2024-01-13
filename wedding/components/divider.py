import reflex as rx

from wedding.styles.colors import Color


def divider() -> rx.Component:
    return rx.divider(
        orientation="horizontal",
        variant="solid",
        border_color=Color.TEXT_DEFAULT.value,
        width="20%",
    )
