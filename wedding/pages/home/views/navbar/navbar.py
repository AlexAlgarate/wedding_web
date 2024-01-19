import reflex as rx

from wedding.styles import Color, Size

from .components import initials_navbar


def navbar() -> rx.Component:
    return rx.center(
        rx.hstack(
            initials_navbar(),
        ),
        box_shadow=f"0px 1px 5px 1px {Color.DEFAULT_OPACITY.value}",
        position="sticky",
        padding_top="0.75em",
        padding_bottom=Size.ZERO.value,
        z_index="999",
        top="0",
        background_color=Color.CONTENT.value,
        class_name="navbar_wedding",
        width="100%",
    )
